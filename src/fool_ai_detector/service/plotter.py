import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ai_human_color = "orangered"
human_ai_color = "crimson"
human_human_color = "gold"
ai_ai_color = "darkorange"


def read_csv(file_path_param):
    return pd.read_csv(file_path_param)


def filter_data(filtered_data_param, text_or_image=None, time_interval=None, pipeline_processors=None):
    """
    whitelist filter of data
    
    :param filtered_data_param:
    :param text_or_image: 
    :param time_interval: 
    :param pipeline_processors: 
    :return: 
    """
    if text_or_image is not None:
        filtered_data_param = filtered_data_param[filtered_data_param['text_or_image'] == text_or_image]
    if time_interval is not None:
        start_time, end_time = pd.to_datetime(time_interval[0]), pd.to_datetime(time_interval[1])
        filtered_data_param = filtered_data_param[
            pd.to_datetime(filtered_data_param['current_date_time']).between(start_time, end_time)]
    if pipeline_processors is not None:
        filtered_data_param = filtered_data_param[filtered_data_param['pipeline_processors'].isin(pipeline_processors)]
    return filtered_data_param

def plot_overview_pipeline_new(data, group_by_param):
    """
    Plot the data in bar diagram

    :param data:
    :param group_by_param: either groupy by processors or evaluators, nothing else!
    """
    # data
    categories = ['ai_human', 'human_human', 'ai_ai', 'human_ai']
    combination_pipeline = []
    ai_ai = []
    human_human = []
    ai_human = []
    human_ai = []

    # grouping
    group_by_list = ["pipeline_processors", "pipeline_evaluator"]
    group_by_list.remove(group_by_param)

    # init
    x_location = []
    last_x_index = 0

    grouped_data_outer = data.groupby([group_by_param])
    for index_outer, (group_name_outer, group_data_outer) in enumerate(grouped_data_outer):
        grouped_data_inner = group_data_outer.groupby([group_by_list[0]])
        n = len(group_data_outer)
        x_location.extend(list(range(last_x_index, last_x_index + n)))
        last_x_index = last_x_index + n
        for index_inner, (group_name_inner, group_data_inner) in enumerate(grouped_data_inner):
            group_data_sum = group_data_inner[categories].sum()

            combination_pipeline.append(group_name_outer[0]+"\n"+group_name_inner[0])

            ai_ai.append(group_data_sum["ai_ai"])
            human_human.append(group_data_sum["human_human"])
            ai_human.append(group_data_sum["ai_human"])
            human_ai.append(group_data_sum["human_ai"])

        last_x_index = last_x_index + 1 # extra group distance

    # show diagram
    bar_width = .5

    bottom_of_bar = [0 for _ in ai_human]
    p1 = plt.bar(x_location, ai_human, bottom=bottom_of_bar, width=bar_width, color="green")

    bottom_of_bar = ai_human
    p2 = plt.bar(x_location, human_human, bottom=bottom_of_bar, width=bar_width, color="grey")

    bottom_of_bar = np.add(human_human, bottom_of_bar).tolist()
    p3 = plt.bar(x_location, ai_ai, bottom=bottom_of_bar, width=bar_width, color="black")

    bottom_of_bar = np.add(ai_ai, bottom_of_bar).tolist()
    p4 = plt.bar(x_location, human_ai, bottom=bottom_of_bar, width=bar_width, color="red")

    # style
    plt.ylabel('Amount')
    plt.xlabel('Processor')
    plt.title('Overview over multiple combination_pipeline')
    plt.xticks(x_location, combination_pipeline)
    plt.legend((p1[0], p2[0], p3[0], p4[0]), categories)

    plt.show()








"""
change the values of the 1.filters and 2.filepath, then run this file.
"""
# example plots
file_path = 'data.csv'
data_frame = read_csv(file_path)

# filters, change these
time_interval_filter = ('2024-01-03 00:00:00', '2024-03-05 00:00:00')
pipeline_processor_filter = ['4']
group_pipeline_processor_filter = ['s_and_p_processor_image', 'poisson_processor_image', 'naive_processor_image', 'naive_processor_image-poisson_processor_image-s_and_p_processor_image']
text_or_image_filter = 'image'

# execute filter
filtered_data = filter_data(data_frame, text_or_image_filter, time_interval_filter, pipeline_processor_filter)
group_filtered_data = filter_data(data_frame, text_or_image_filter, time_interval_filter,
                                  group_pipeline_processor_filter)

# execute examples
#group by: 1. pipeline_processors 2. pipeline_evaluator
group_by = "pipeline_processors"
plot_overview_pipeline_new(group_filtered_data, group_by)

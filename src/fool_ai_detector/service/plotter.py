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
        filtered_data_param = filtered_data_param[pd.to_datetime(filtered_data_param['current_date_time']).between(start_time, end_time)]
    if pipeline_processors is not None:
        filtered_data_param = filtered_data[filtered_data['pipeline_processors'].isin(pipeline_processors)]
    return filtered_data_param

def plot_single_pipeline(filtered_data_param):
    """
    if you want to plot a graph for only one pipeline use this method
    
    :param filtered_data_param: 
    :return: 
    """
    headers_to_plot = ['runs', 'human_human', 'ai_ai', 'ai_human', 'human_ai']
    selected_header_sums = filtered_data_param[headers_to_plot].sum()
    bar_width = 0.5

    plt.figure(figsize=(10, 6))

    for header in headers_to_plot:
        color = 'blue'
        if header == "ai_human":
            color = ai_human_color
        elif header == "human_ai":
            color = human_ai_color
        elif header == "human_human":
            color = human_human_color
        elif header == "ai_ai":
            color = ai_ai_color
        plt.bar(header, selected_header_sums[header], alpha=0.7, width=bar_width, align='center', color=color)

    plt.text(0.7, 0.75, 'generator: ' + str(filtered_data_param["pipeline_generator"].values[0]) + "\n"
             +'processors: ' + str(filtered_data_param["pipeline_processors"].values) + "\n"
             +'evaluator: ' + str(filtered_data_param["pipeline_evaluator"].values[0]),
             ha='center', va='center', fontsize=12,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'), transform=plt.gcf().transFigure)
    plt.xlabel('types of runs, example: human_human means that the original image got detected as human and the augmented image also.')
    plt.ylabel('Count')
    plt.title('Header')
    plt.grid(True)

    plt.show()



def plot_overview_pipeline(filtered_data_param):
    """
    if you want to have an overview over many different pipelines, use this method

    :param filtered_data_param:
    :return:
    """
    headers_to_plot = ['human_human', 'ai_ai', 'ai_human', 'human_ai']

    grouped_filtered_data = filtered_data_param.groupby('pipeline_processors')
    bar_width = 0.3
    num_groups = len(grouped_filtered_data)
    group_positions = np.arange(num_groups)

    plt.figure(figsize=(15, 8))
    label = False
    for i, (group_name, group_data) in enumerate(grouped_filtered_data):
        bottom_values = np.zeros(len(headers_to_plot))
        grouped_filtered_data_header_sum = group_data[headers_to_plot].sum()
        for j, header in enumerate(headers_to_plot):
            color = 'blue'
            if header == "ai_human":
                color = ai_human_color
            elif header == "human_ai":
                color = human_ai_color
            elif header == "human_human":
                color = human_human_color
            elif header == "ai_ai":
                color = ai_ai_color
            if not label:
                plt.bar(group_positions[i], grouped_filtered_data_header_sum[header], alpha=0.7, width=bar_width, align='center', color=color,
                    bottom=bottom_values, label=f'{header}')
            else:
                plt.bar(group_positions[i], grouped_filtered_data_header_sum[header], alpha=0.7, width=bar_width, align='center', color=color,
                    bottom=bottom_values)
            bottom_values += grouped_filtered_data_header_sum[header]
        label = True

    plt.xlabel('Alle Header zusammengefasst')
    plt.ylabel('Anteile')
    plt.title('Alle Header in einem Balken')
    plt.xticks(group_positions, grouped_filtered_data.groups.keys())
    plt.legend()
    plt.grid(True)

    plt.show()
    
# example plots
file_path = 'data.csv'
data_frame = read_csv(file_path)

# filter
time_interval_filter = ('2024-01-03 00:00:00', '2024-01-05 00:00:00')
pipeline_processor_filter = ['4']
group_pipeline_processor_filter = ['naive_processor_image', '1', '2', '3', '4']
text_or_image_filter = 'image'

# execute filter
filtered_data = filter_data(data_frame, text_or_image_filter, time_interval_filter, pipeline_processor_filter)
group_filtered_data = filter_data(data_frame, text_or_image_filter, time_interval_filter, group_pipeline_processor_filter)

# execute examples
plot_single_pipeline(filtered_data)
plot_overview_pipeline(group_filtered_data)

from datetime import datetime
import csv


class CSVWriter:
    """
    CSVWriter class
    """
    current_date_time = ""
    pipeline_generator = ""
    pipeline_processors = ""
    pipeline_evaluator = ""
    text_or_image = ""
    runs = 0
    human_human = 0
    ai_ai = 0
    ai_human = 0
    human_ai = 0

    def __init__(self, generator, processors, evaluator, text_or_image, runs):
        """
        Constructor for CSV Writer

        :param generator: the generator used
        :param processors: the processors used
        :param evaluator: the evaluator used
        :param text_or_image: image/text
        :param runs: The number of images for this run tested
        """
        self.current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.pipeline_generator = generator
        self.pipeline_processors = processors
        self.pipeline_evaluator = evaluator
        self.text_or_image = text_or_image
        self.runs = runs

    def increase_human_human(self):
        """
        This Method increases the variable that counts the times that the original image and the processed image
        came to the result that it was human-generated
        """
        self.human_human = self.human_human + 1

    def increase_ai_ai(self):
        """
        This Method increases the variable that counts the times that the original image and the processed image
        came to the result that it was AI-generated
        """
        self.ai_ai = self.ai_ai + 1

    def increase_human_ai(self):
        """
        This Method increases the variable that counts the times that the original image was human-generated and the
        processed image was AI-generated
        """
        self.human_ai = self.human_ai + 1

    def increase_ai_human(self):
        """
        This Method increases the variable that counts the times that the original image was AI-generated and the
        processed image was human-generated
        """
        self.ai_human = self.ai_human + 1

    def write_to_csv(self, filename='data.csv'):
        """
        This method writes the current data into a file (filename)
        :param filename: the filename of the generated file
        """
        try:
            with open(filename, 'r', newline='') as file:
                header = next(csv.reader(file))
        except FileNotFoundError:
            header = ['current_date_time', 'pipeline_generator', 'pipeline_processors',
                      'pipeline_evaluator', 'text_or_image', 'runs', 'human_human', 'ai_ai', 'ai_human', 'human_ai']

        data = [getattr(self, attribute) for attribute in header]

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            # new file, write header
            if file.tell() == 0:
                writer.writerow(header)
            writer.writerow(data)

"""
Text processor based on the results of all the different processors
"""
from pathlib import Path

from fool_ai_detector.model.processor import Processor


class FinalTextProcessor(Processor):
    """
    Text processor that uses...
    - [Processor 1]
    - [Processor 2]
    - ...
    """

    def process(self, input_file_path, output_file_path):
        """
        Augments a text by ...

        :param input_file_path: path to the file, that should be processed
        :param output_file_path: path where the processed file should be saved
        """
        text = Path(input_file_path).read_text(encoding="utf-8")
        augmented_text = text + "Hello"
        Path(output_file_path).write_text(augmented_text, encoding="utf-8")

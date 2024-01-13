"""
Text processor based on the results of all the different processors
"""
from pathlib import Path

from fool_ai_detector.service.typo_text_processor import TypoProcessor
from fool_ai_detector.model.processor import Processor


class FinalTextProcessor(Processor):
    """
    Text processor that uses
    - Typo processor
    """

    def process(self, input_file_path, output_file_path):
        """
        Augments a text by generating some typos in it

        :param input_file_path: path to the file, that should be processed
        :param output_file_path: path where the processed file should be saved
        """
        typo_processor = TypoProcessor()
        typo_processor.process(input_file_path, output_file_path)

"""
Text processor based on the idea of using two white-spaces instead of one
"""
from pathlib import Path

from fool_ai_detector.model.processor import Processor


class DoubleWhitespaceProcessor(Processor):
    """
    Text processor that uses two white-spaces instead of one
    """

    def process(self, input_file_path, output_file_path):
        """
        Replaces every occurrence of a white-space with double white-space to augment a text.

        :param input_file_path: path to the file, that should be processed
        :param output_file_path: path where the processed file should be saved
        """
        text = Path(input_file_path).read_text(encoding="utf-8")
        augmented_text = text.replace(" ", "  ")
        Path(output_file_path).write_text(augmented_text, encoding="utf-8")

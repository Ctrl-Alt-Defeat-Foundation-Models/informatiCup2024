"""
Processor based on the idea of making mistakes while typing
"""
from pathlib import Path
import typo

from fool_ai_detector.model.processor import Processor


class TypoProcessor(Processor):
    """
    Typo Processor
    """

    def process(self, input_file_path, output_file_path, words_per_error=5):
        """
        Add some typos to the generated text and saves it.
        :param input_file_path: path to the file, that should be processed
        :param output_file_path: path where the processed file should be saved
        :param words_per_error: how many words should have a typo
        """
        text = Path(input_file_path).read_text()
        augmented_text = ''

        text_array = text.split()
        loop_invariant = 0
        for word in text_array:
            if loop_invariant % words_per_error == 0:
                error_string = typo.StrErrer(word, seed=31)
                augmented_text += error_string.nearby_char(preservelast=True, preservefirst=True).result
            else:
                augmented_text += word
            loop_invariant += 1
            augmented_text += ' '

        Path(output_file_path).write_text(augmented_text)

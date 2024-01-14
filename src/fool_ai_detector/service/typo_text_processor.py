"""
Processor based on the idea of making mistakes while typing (typo)
"""
import math
import random
from pathlib import Path
import typo

from fool_ai_detector.model.processor import Processor


class TypoProcessor(Processor):
    """
    Typo Processor
    """

    def process(self, input_file_path, output_file_path, mistake_percentage=15):
        """
        Add some typos to the generated text and saves it.

        :param input_file_path: path to the file, that should be processed
        :param output_file_path: path where the processed file should be saved
        :param mistake_percentage: percentage of mistakes in the text
        """
        text = Path(input_file_path).read_text(encoding="utf-8")
        augmented_text = ''

        text_array = text.split()
        number_words = len(text_array)
        percentage = math.ceil(number_words/100 * mistake_percentage)
        number_mistakes = random.sample(range(0, number_words), percentage)
        loop_invariant = 0
        for word in text_array:
            if loop_invariant in number_mistakes:
                type_of_error = random.randint(0, 7)
                error_string = typo.StrErrer(word, seed=31)
                match type_of_error:
                    case 0:
                        augmented_text += error_string.nearby_char(preservelast=True, preservefirst=True).result
                    case 1:
                        augmented_text += error_string.char_swap(preservelast=False, preservefirst=False).result
                    case 2:
                        augmented_text += error_string.missing_char(preservelast=False, preservefirst=True).result
                    case 3:
                        augmented_text += error_string.extra_char(preservelast=False, preservefirst=True).result
                    case 4:
                        augmented_text += error_string.similar_char().result
                    case 6:
                        augmented_text += error_string.random_space().result
                    case 7:
                        augmented_text += error_string.repeated_char().result
                    case 8:
                        augmented_text += error_string.unichar().result

            else:
                augmented_text += word
            loop_invariant += 1
            augmented_text += ' '

        Path(output_file_path).write_text(augmented_text, encoding="utf-8")

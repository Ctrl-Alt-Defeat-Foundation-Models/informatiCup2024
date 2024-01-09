"""
Text processor based on the idea of translating a text into another language and back
"""
from pathlib import Path
import translators as ts

from fool_ai_detector.model.processor import Processor


class TranslatorProcessor(Processor):
    """
    Translator Processor
    """

    def process(self, input_file_path, output_file_path):
        """
        Translates the input file into another language and then back to english.

        :param input_file_path: path to the file, that should be processed
        :param output_file_path: path where the processed file should be saved
        """
        text = Path(input_file_path).read_text(encoding="utf-8")

        text_parts = split_and_combine(text)
        translated_text_fr = ''
        for text_part in text_parts:
            translated_text_fr = translated_text_fr + ts.translate_text(text_part, to_language='fr')

        text_parts = split_and_combine(translated_text_fr)
        augmented_text = ''
        for text_part in text_parts:
            augmented_text = augmented_text + ts.translate_text(text_part, to_language='en')

        Path(output_file_path).write_text(augmented_text, encoding="utf-8")


def split_and_combine(text, max_length=1000):
    """
    Cuts the text into pieces and combines it back together into parts that do not exceed the maximum length
    :param text: the text to be split
    :param max_length: the maximum length of a combined text
    """
    sentences = text.split('. ')

    parts = []
    current_part = ""

    for sentence in sentences:
        if len(current_part) + len(sentence) <= max_length:
            current_part += sentence + '. '
        else:
            parts.append(current_part)
            current_part = sentence + '. '

    parts.append(current_part)

    return parts

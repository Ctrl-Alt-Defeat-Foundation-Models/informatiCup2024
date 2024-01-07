from pathlib import Path
import translators as ts

from fool_ai_detector.model.processor import Processor


class TranslatorProcessor(Processor):
    def process(self, input_file_path, output_file_path):
        """
        Translates the input file into another language and then back to english.
        """
        text = Path(input_file_path).read_text()

        text_parts = split_and_combine(text)
        translated_text_fr = ''
        for text_part in text_parts:
            translated_text_fr = translated_text_fr + ts.translate_text(text_part, to_language='fr')

        text_parts = split_and_combine(translated_text_fr)
        augmented_text = ''
        for text_part in text_parts:
            augmented_text = augmented_text + ts.translate_text(text_part, to_language='en')

        Path(output_file_path).write_text(augmented_text)


def split_and_combine(text, max_length=500):
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

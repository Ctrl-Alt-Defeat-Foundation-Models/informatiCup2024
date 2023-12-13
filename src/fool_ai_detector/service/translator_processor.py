from pathlib import Path
import translators as ts

from fool_ai_detector.model.processor import Processor


class TranslatorProcessor(Processor):
    def process(self, input_file_path, output_file_path):
        """
        Translates the input file into another language and then back to english.
        """
        text = Path(input_file_path).read_text()
        translated_text = ts.translate_text(text, to_language='fr')
        augmented_text = ts.translate_text(translated_text, to_language='en')
        Path(output_file_path).write_text(augmented_text)

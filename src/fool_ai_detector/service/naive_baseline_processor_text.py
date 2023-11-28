from pathlib import Path

from fool_ai_detector.model.processor import Processor


class NaiveBaselineProcessorText(Processor):
    def process(self, input_file_path, output_file_path):
        """
        Replaces every occurrence of a white space with double white space to augment a text.
        """
        text = Path(input_file_path).read_text()
        augmented_text = text.replace(" ", "  ")
        Path(output_file_path).write_text(augmented_text)

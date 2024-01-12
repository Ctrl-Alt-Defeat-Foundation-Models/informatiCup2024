import os
from pathlib import Path

from fool_ai_detector.service.final_text_processor import FinalTextProcessor


class TestDoubleWhitespaceProcessor:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_generator_file_path = os.path.join(base_path_this_class, '..', '..', '..', 'src',
                                              'fool_ai_detector', 'resources', 'ai_gen_text', 'alpen.txt')
    output_processor_directory_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                                   'final_text_processor_texts')
    output_processor_file_path = os.path.join(output_processor_directory_path, 'processed_alpen.txt')

    def set_up(self):
        """
        Helper method: This method creates the test folders.
        """
        if not os.path.exists(self.output_processor_directory_path):
            os.makedirs(self.output_processor_directory_path)

    def test_final_text_process(self):
        self.set_up()

        final_text_processor = FinalTextProcessor()
        final_text_processor.process(self.output_generator_file_path, self.output_processor_file_path)

        origin_text = Path(self.output_generator_file_path).read_text(encoding="utf-8")
        processed_text = Path(self.output_processor_file_path).read_text(encoding="utf-8")

        assert origin_text != processed_text

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method clears the used test folders.
        """
        filelist_output = os.listdir(self.output_processor_directory_path)
        for file in filelist_output:
            os.remove(os.path.join(self.output_processor_directory_path, file))

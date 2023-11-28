import os
from pathlib import Path

from fool_ai_detector.service.naive_baseline_processor_text import NaiveBaselineProcessorText


class TestNaiveBaselineProcessorText:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_generator_file_path = os.path.join(base_path_this_class, '..', '..', '..', 'src',
                                              'fool_ai_detector', 'resources', 'ai_gen_text', 'alpen.txt')
    output_processor_directory_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                                   'naive_processor_texts')
    output_processor_file_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                              'naive_processor_images', 'processed_alpen.txt')

    def set_up(self):
        """
        Helper method: This method creates the test folders.
        """
        if not os.path.exists(self.output_processor_directory_path):
            os.makedirs(self.output_processor_directory_path)

    def test_process(self):
        self.set_up()

        naive_baseline_processor = NaiveBaselineProcessorText()
        naive_baseline_processor.process(self.output_generator_file_path, self.output_processor_file_path)

        origin_text_occurrences = Path(self.output_generator_file_path).read_text().count(' ')
        augmented_text_occurrences = Path(self.output_processor_file_path).read_text().count('  ')

        assert origin_text_occurrences == augmented_text_occurrences

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method clears the used test folders.
        """
        filelist_output = os.listdir(self.output_processor_directory_path)
        for file in filelist_output:
            os.remove(os.path.join(self.output_processor_directory_path, file))

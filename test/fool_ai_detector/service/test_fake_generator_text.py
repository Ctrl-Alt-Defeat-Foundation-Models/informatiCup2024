from fool_ai_detector.service.fake_generator_text import FakeGeneratorText
import pytest
import os


class TestFakeGeneratorText:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_dir_path = os.path.join(base_path_this_class, '..', '..', 'test_output', 'fake_generator_texts')
    output_file_path = os.path.join(base_path_this_class, '..', '..', 'test_output', 'fake_generator_texts', 'generated_text.txt')

    def set_up(self):
        """
        Helper method: This method creates the output test folder.
        """
        if not os.path.exists(self.output_dir_path):
            os.makedirs(self.output_dir_path)

    def test_normal_generation(self):
        self.set_up()
        self.clear_test_output()

        fake_generator = FakeGeneratorText()
        fake_generator.generate(self.output_file_path)

        filelist = os.listdir(self.output_dir_path)
        assert len(filelist) == 1

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method makes clears the test output folder.
        """
        filelist = os.listdir(self.output_dir_path)
        for file in filelist:
            os.remove(os.path.join(self.output_dir_path, file))

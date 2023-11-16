from fool_ai_detector.service.fake_generator_picture import FakeGeneratorPicture
import pytest
import os


class TestFakeGeneratorPicture:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(base_path_this_class, '..', '..', 'test_output', 'fake_generator_pictures')

    def set_up(self):
        """
        Helper method: This method creates the output test folder.
        """
        if not os.path.exists(self.output_file_path):
            os.mkdir(self.output_file_path)

    def test_normal_generation(self):
        self.set_up()
        self.clear_test_output()

        fake_generator = FakeGeneratorPicture()
        fake_generator.generate(self.output_file_path)

        filelist = os.listdir(self.output_file_path)
        assert len(filelist) == 1

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method makes clears the test output folder.
        """
        filelist = os.listdir(self.output_file_path)
        for file in filelist:
            os.remove(os.path.join(self.output_file_path, file))

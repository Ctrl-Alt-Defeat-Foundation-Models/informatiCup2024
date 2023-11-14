from service.fake_generator_text import FakeGeneratorText
import unittest
import os


class TestFakeGeneratorText(unittest.TestCase):
    output_file_path = "../../test_output/fake_generator_texts/"

    def setUp(self):
        if not os.path.exists(self.output_file_path):
            os.mkdir(self.output_file_path)

    def test_normal_generation(self):
        self.clear_test_output()

        fake_generator = FakeGeneratorText()
        fake_generator.generate(self.output_file_path)

        filelist = os.listdir(self.output_file_path)
        self.assertEqual(len(filelist), 1)

        self.clear_test_output()

    def clear_test_output(self):
        """
            Helper method: This method makes clears the test output folder.
        """
        filelist = os.listdir(self.output_file_path)
        for file in filelist:
            os.remove(os.path.join(self.output_file_path, file))

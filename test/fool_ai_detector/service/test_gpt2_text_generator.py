import os

from fool_ai_detector.service.gpt2_text_generator import GPT2TextGenerator


class TestGPT2Generator:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_dir_path = os.path.join(base_path_this_class, '..', '..', 'test_output', 'gpt2_generator_texts')

    def set_up(self):
        """
        Helper method: This method creates the output test folder.
        """
        if not os.path.exists(self.output_dir_path):
            os.makedirs(self.output_dir_path)

    def test_gpt2_generation(self):
        self.set_up()
        self.clear_test_output()

        gpt2_generator_generator = GPT2TextGenerator()
        gpt2_generator_generator.generate(os.path.join(self.output_dir_path, 'test_text.txt'),
                                          "The University of Stuttgart is")

        filelist = os.listdir(self.output_dir_path)
        assert len(filelist) == 1

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method clears the test output folder.
        """
        filelist = os.listdir(self.output_dir_path)
        for file in filelist:
            os.remove(os.path.join(self.output_dir_path, file))

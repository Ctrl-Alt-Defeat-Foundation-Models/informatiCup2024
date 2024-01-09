import os

from fool_ai_detector.service.dalle_image_generator import DalleImageGenerator


class TestDalleImageGenerator:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                    'dalle_generator_images')

    def set_up(self):
        """
        Helper method: This method creates the output test folder.
        """
        if not os.path.exists(self.output_file_path):
            os.makedirs(self.output_file_path)

    def test_dalle_generation(self):
        self.set_up()
        self.clear_test_output()

        dalle_generator = DalleImageGenerator()
        dalle_generator.generate(os.path.join(self.output_file_path, 'test_image.png'),
                                 "Generate a realistic image of a cat on a bike")

        filelist = os.listdir(self.output_file_path)
        assert len(filelist) == 1

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method clears the test output folder.
        """
        filelist = os.listdir(self.output_file_path)
        for file in filelist:
            os.remove(os.path.join(self.output_file_path, file))

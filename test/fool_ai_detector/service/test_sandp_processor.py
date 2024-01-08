import os
import skimage.io
import numpy

from fool_ai_detector.service.sandp_processor import SAndPProcessor


class TestSAndPProcessor:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_generator_file_path = os.path.join(base_path_this_class, '..', '..', '..', 'src',
                                              'fool_ai_detector', 'resources', 'ai_gen_images', 'clownfish.png')
    output_processor_directory_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                                   's_and_p_processor_images')
    output_processor_file_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                              's_and_p_processor_images', 'processed_clownfish.png')

    def set_up(self):
        """
        Helper method: This method creates the test folders.
        """
        if not os.path.exists(self.output_processor_directory_path):
            os.makedirs(self.output_processor_directory_path)

    def test_process(self):
        self.set_up()

        sandp_processor = SAndPProcessor()
        sandp_processor.process(self.output_generator_file_path, self.output_processor_file_path)

        image_input = skimage.io.imread(self.output_generator_file_path)
        image_output = skimage.io.imread(self.output_processor_file_path)

        assert not numpy.array_equal(image_input, image_output)

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method clears the used test folders.
        """
        filelist_output = os.listdir(self.output_processor_directory_path)
        for file in filelist_output:
            os.remove(os.path.join(self.output_processor_directory_path, file))

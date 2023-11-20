import math
import os

import skimage.io

from fool_ai_detector.service.fake_generator_picture import FakeGeneratorPicture
from fool_ai_detector.service.naive_baseline_processor_picture import NaiveBaselineProcessorImage


class TestNaiveBaselineProcessorPicture:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_generator_file_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                              'fake_generator_pictures')
    output_processor_file_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                              'naive_processor_pictures')

    def set_up(self):
        """
        Helper method: This method creates the test folders.
        """
        if not os.path.exists(self.output_generator_file_path):
            os.makedirs(self.output_generator_file_path)

        if not os.path.exists(self.output_processor_file_path):
            os.makedirs(self.output_processor_file_path)

    def test_process(self):
        self.set_up()

        fake_generator = FakeGeneratorPicture()
        fake_generator.generate(self.output_generator_file_path)

        listdir_generator_output = os.listdir(self.output_generator_file_path)
        image_name = listdir_generator_output[0]
        generated_image_path = ''
        if os.path.isfile(os.path.join(self.output_generator_file_path, image_name)):
            generated_image_path = os.path.join(self.output_generator_file_path, image_name)

        naive_baseline_processor = NaiveBaselineProcessorImage()
        naive_baseline_processor.process(generated_image_path, self.output_processor_file_path)

        image_input = skimage.io.imread(generated_image_path)
        image_output = skimage.io.imread(os.path.join(self.output_processor_file_path, 'naive_processed_picture.png'))

        assert not math.isinf(skimage.metrics.peak_signal_noise_ratio(image_input, image_output))

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method clears the used test folders.
        """
        filelist_input = os.listdir(self.output_generator_file_path)
        for file in filelist_input:
            os.remove(os.path.join(self.output_generator_file_path, file))

        filelist_output = os.listdir(self.output_processor_file_path)
        for file in filelist_output:
            os.remove(os.path.join(self.output_processor_file_path, file))

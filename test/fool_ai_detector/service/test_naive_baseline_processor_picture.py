import math
import os
import skimage.io

from fool_ai_detector.service.naive_baseline_processor_picture import NaiveBaselineProcessorImage


class TestNaiveBaselineProcessorPicture:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_generator_file_path = os.path.join(base_path_this_class, '..', '..', '..', 'src',
                                              'fool_ai_detector', 'resources', 'ai_gen_images', 'clownfish.png')
    output_processor_directory_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                                   'naive_processor_pictures')
    output_processor_file_path = os.path.join(base_path_this_class, '..', '..', 'test_output',
                                              'naive_processor_pictures', 'processed_clownfish.png')

    def set_up(self):
        """
        Helper method: This method creates the test folders.
        """
        if not os.path.exists(self.output_processor_directory_path):
            os.makedirs(self.output_processor_directory_path)

    def test_process(self):
        self.set_up()

        naive_baseline_processor = NaiveBaselineProcessorImage()
        naive_baseline_processor.process(self.output_generator_file_path, self.output_processor_file_path)

        image_input = skimage.io.imread(self.output_generator_file_path)
        image_output = skimage.io.imread(self.output_processor_file_path)

        assert not math.isinf(skimage.metrics.peak_signal_noise_ratio(image_input, image_output))

        self.clear_test_output()

    def clear_test_output(self):
        """
        Helper method: This method clears the used test folders.
        """
        filelist_output = os.listdir(self.output_processor_file_path)
        for file in filelist_output:
            os.remove(os.path.join(self.output_processor_file_path, file))

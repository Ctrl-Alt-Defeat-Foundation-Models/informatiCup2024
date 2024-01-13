"""
Final image processor based on the results of the tests
"""

from fool_ai_detector.model.processor import Processor
from fool_ai_detector.service.gaussian_processor import GaussianProcessor
from fool_ai_detector.service.s_and_p_processor import SAndPProcessor


class FinalImageProcessor(Processor):
    """
    Image processor that uses
    - gaussian noise
    - salt and pepper noise
    """

    def process(self, input_file_path, output_file_path):
        """
        Augments an image by adding gaussian and salt and pepper noise

        :param input_file_path: path to the file, that should be processed
        :param output_file_path: path where the processed file should be saved
        """
        GaussianProcessor().process(input_file_path, output_file_path)
        SAndPProcessor().process(output_file_path, output_file_path)

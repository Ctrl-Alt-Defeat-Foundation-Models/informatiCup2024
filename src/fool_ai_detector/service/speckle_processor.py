"""
Speckle noise image processor
"""
import numpy as np
import skimage

from fool_ai_detector.model.processor import Processor


class SpeckleProcessor(Processor):
    """
    Speckle Processor
    """
    def process(self, input_file_path, output_file_path):
        """
        Adds speckle noise to an image to augment it.
        :param input_file_path: path to the file, that should be processed
        :param output_file_path: path where the processed file should be saved
        """
        image = skimage.io.imread(input_file_path)
        processed_image = skimage.util.random_noise(image, mode='speckle', clip=True)
        processed_image = (processed_image * 255).astype(np.uint8)
        skimage.io.imsave(output_file_path, processed_image, check_contrast=False)

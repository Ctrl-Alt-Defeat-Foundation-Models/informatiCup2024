import os
import numpy as np
import skimage

from fool_ai_detector.model.processor import Processor


class NaiveBaselineProcessorImage(Processor):
    def process(self, input_file_path, output_file_path):
        """
        Adds some random noise to an image to augment it.
        """
        image = skimage.io.imread(input_file_path)
        processed_image = skimage.util.random_noise(image, mode='gaussian', clip=True)
        processed_image = (processed_image * 255).astype(np.uint8)
        skimage.io.imsave(output_file_path, processed_image, check_contrast=False)
import skimage
import os
import random

from fool_ai_detector.model.generator import Generator


class FakeGeneratorImage(Generator):
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_path_this_class, '..', 'resources', 'ai_gen_images')
    images = []

    def __init__(self):
        for image in os.listdir(self.dir_path):
            if os.path.isfile(os.path.join(self.dir_path, image)):
                self.images.append(os.path.join(self.dir_path, image))

    def generate(self, prompt, output_file_path):
        """
        Method that takes one random image of the ai_gen_image directory and puts it in another directory.
        """
        random_image_index = random.randint(0, len(self.images) - 1)
        random_image_path = self.images[random_image_index]
        random_image_name = os.path.basename(random_image_path)
        random_image = skimage.io.imread(random_image_path)
        if not os.path.exists(output_file_path):
            os.makedirs(output_file_path)
        skimage.io.imsave(os.path.join(output_file_path, random_image_name), random_image, check_contrast=False)


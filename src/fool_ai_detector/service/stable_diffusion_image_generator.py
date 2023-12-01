"""
Generator based on the Stable Diffusion model
"""
import skimage
import torch
from diffusers import StableDiffusionPipeline
from fool_ai_detector.model.generator import Generator


class StableDiffusionImageGenerator(Generator):
    """
    Base class for a Generator
    """

    def generate(self, prompt, output_file_path):
        """
        Generates an image out of a prompt
        :param prompt: Prompt to generate the image from
        :param output_file_path: Path, where the generated image is saved
        """

        pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
        pipe = pipe.to("cuda")

        image = pipe(prompt).images[0]
        skimage.io.imsave(output_file_path, image, check_contrast=False)

"""
Generator based on the Stable Diffusion model
"""
import torch.cuda
from diffusers import StableDiffusionPipeline

from fool_ai_detector.model.generator import Generator


class StableDiffusionImageGenerator(Generator):
    """
    Base class for a Generator
    """

    def generate(self, output_file_path, prompt="Generate a realistic random image"):
        """
        Generates an image out of a prompt
        :param prompt: Prompt to generate the image from
        :param output_file_path: Path, where the generated image is saved
        """

        if torch.cuda.is_available():
            pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
            pipe.to("cuda")
        else:
            pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

        image = pipe(prompt).images[0]
        image.save(output_file_path)

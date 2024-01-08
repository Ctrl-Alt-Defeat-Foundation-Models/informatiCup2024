"""
Generator based on the Dall-E model
"""
import torch.cuda
from diffusers import AutoPipelineForText2Image

from fool_ai_detector.model.generator import Generator


class DalleImageGenerator(Generator):
    """
    Class for the Dall-E image generator
    """

    def generate(self, output_file_path, prompt="Generate a realistic random image"):
        """
        Generates an image out of a prompt
        :param prompt: Prompt to generate the image from
        :param output_file_path: Path, where the generated image is saved
        """

        if torch.cuda.is_available():
            pipe = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalle', torch_dtype=torch.float16,
                                                             offload_state_dict=True).to('cuda')
        else:
            pipe = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalle')

        image = pipe(prompt).images[0]
        image.save(output_file_path)

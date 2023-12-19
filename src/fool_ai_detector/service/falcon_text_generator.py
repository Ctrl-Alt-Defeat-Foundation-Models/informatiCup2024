"""
Generator based on the Falcon-RW-1B  model
"""
from pathlib import Path

import torch.cuda
from transformers import pipeline

from fool_ai_detector.model.generator import Generator


class FalconRW1BTextGenerator(Generator):
    """
    class for a Generator based on the Falcon-RW  model
    """

    def generate(self, output_file_path, prompt="Generate a random text:"):
        """
        Generates a text out of a prompt

        :param prompt: Prompt to generate the text from
        :param output_file_path: Path, where the generated text is saved
        """
        if torch.cuda.is_available():
            pipe = pipeline("text-generation", model="tiiuae/falcon-rw-1b", top_k=1, device=0)
        else:
            pipe = pipeline("text-generation", model="tiiuae/falcon-rw-1b", top_k=1)

        result = pipe(prompt)
        text = result[0]["generated_text"]
        Path(output_file_path).write_text(text)

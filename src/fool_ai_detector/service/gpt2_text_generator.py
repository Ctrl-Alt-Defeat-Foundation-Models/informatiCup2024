"""
Generator based on the GPT2 model
"""
from pathlib import Path

import torch.cuda
from transformers import pipeline

from fool_ai_detector.model.generator import Generator


class GPT2TextGenerator(Generator):
    """
    Base class for a Generator
    """

    def generate(self, output_file_path, prompt="Generate a random text"):
        """
        Generates a text out of a prompt

        :param prompt: Prompt to generate the text from
        :param output_file_path: Path, where the generated text is saved
        """
        if torch.cuda.is_available():
            pipe = pipeline("text-generation", model="gpt2-large", max_length=514, pad_token_id=50256, device=0)
        else:
            pipe = pipeline("text-generation", model="gpt2-large", max_length=514, pad_token_id=50256)

        text = pipe(prompt)[0]["generated_text"]
        Path(output_file_path).write_text(text, encoding="utf-8")

"""
Generator based on the GPT2 model
"""
from pathlib import Path

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
        pipe = pipeline("text-generation", model="gpt2-large", max_length=514)

        text = pipe(prompt)[0]["generated_text"]
        print(text)
        Path(output_file_path).write_text(text)

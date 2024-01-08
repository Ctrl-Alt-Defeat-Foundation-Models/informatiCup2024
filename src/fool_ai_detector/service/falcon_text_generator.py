"""
Generator based on the Falcon-RW-1B  model
"""
from pathlib import Path

import torch.cuda
import transformers
from transformers import AutoTokenizer

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
        model = "tiiuae/falcon-rw-1b"

        tokenizer = AutoTokenizer.from_pretrained(model)
        pipeline = transformers.pipeline("text-generation", model=model, tokenizer=tokenizer,
                                         torch_dtype=torch.bfloat16, device_map="auto")
        sequences = pipeline("The University of Stuttgart is", max_length=200, do_sample=True,
                             eos_token_id=tokenizer.eos_token_id, pad_token_id=2)

        Path(output_file_path).write_text(sequences[0]["generated_text"])

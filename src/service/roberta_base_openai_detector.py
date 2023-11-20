"""
Evaluator based on the roberta_base_openai_detector
"""
from model.evaluator import Evaluator
from transformers import pipeline


class RobertaBaseEvaluator(Evaluator):
    """
    Base class for an Evaluator
    """

    def evaluate(self, input_file_path) -> bool:
        """
        Evaluates a given text based on the specific detector
        """
        text = input_file_path.read_text()
        pipe = pipeline("text-classification", model="roberta-base-openai-detector")
        output = pipe(text)
        label = output[0]["label"]
        if label == "Real":
            return False
        else:
            return True

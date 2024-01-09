"""
Evaluator based on the roberta_base_openai_detector
"""
from transformers import pipeline

from fool_ai_detector.model.evaluator import Evaluator


class RobertaBaseEvaluator(Evaluator):
    """
    RobertaBase Evaluator
    """

    def evaluate(self, input_file_path) -> bool:
        """
        Evaluates a given text based on the specific detector

        :param input_file_path: path to the file, that should be evaluated
        :return: bool; true = fake, false = real
        """
        file = open(input_file_path, "r")
        text = file.read()
        pipe = pipeline("text-classification", model="roberta-base-openai-detector", max_length=512, truncation=True)
        output = pipe(text)
        label = output[0]["label"]
        if label == "Real":
            return False
        else:
            return True

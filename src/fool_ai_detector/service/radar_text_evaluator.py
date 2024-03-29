"""
Evaluator based on the TrustSafeAI/RADAR-Vicuna-7B
"""
from transformers import pipeline

from fool_ai_detector.model.evaluator import Evaluator


class RadarEvaluator(Evaluator):
    """
    Radar Evaluator
    """

    def evaluate(self, input_file_path) -> bool:
        """
        Evaluates a given text based on the specific detector

        :param input_file_path: path to the file, that should be evaluated
        :return: bool; true = fake, false = real
        """
        file = open(input_file_path, "r", encoding="utf-8")
        text = file.read()
        pipe = pipeline("text-classification", model="TrustSafeAI/RADAR-Vicuna-7B", max_length=512, truncation=True)
        output = pipe(text)
        label = output[0]["label"]
        if label == "Real":
            return False
        else:
            return True

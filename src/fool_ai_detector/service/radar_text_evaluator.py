"""
Evaluator based on the TrustSafeAI/RADAR-Vicuna-7B
"""
from fool_ai_detector.model.evaluator import Evaluator
from transformers import pipeline


class RadarEvaluator(Evaluator):
    """
    Base class for an Evaluator
    """

    def evaluate(self, input_file_path) -> bool:
        """
        Evaluates a given text based on the specific detector
        :param input_file_path: path to the file, that should be evaluated
        :return: bool; true = fake, false = real
        """
        file = open(input_file_path, "r")
        text = file.read()
        pipe = pipeline("text-classification", model="TrustSafeAI/RADAR-Vicuna-7B")
        output = pipe(text)
        label = output[0]["label"]
        if label == "Real":
            return False
        else:
            return True

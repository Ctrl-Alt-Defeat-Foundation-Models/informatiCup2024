"""
Evaluator based on the AI-image-detector by Nahrawy
"""
from fool_ai_detector.model.evaluator import Evaluator
from transformers import pipeline


class NahrawyEvaluator(Evaluator):
    """
    Nahrawy image Evaluator
    """

    def evaluate(self, input_file_path) -> bool:
        """
        Evaluates a given image based on the specific detector
        :param input_file_path: path to the file, that should be evaluated
        :return: bool; true = fake, false = real
        """
        pipe = pipeline("image-classification", model="Nahrawy/AIorNot")
        output = pipe(input_file_path)
        return output[0]["label"] == "ai"

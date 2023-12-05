"""
Evaluator based on the AI-image-detector by umm-maybe
"""
from fool_ai_detector.model.evaluator import Evaluator
from transformers import pipeline


class UmmMaybeEvaluator(Evaluator):
    """
    Umm-Maybe Evaluator
    """

    def evaluate(self, input_file_path) -> bool:
        """
        Evaluates a given image based on the specific detector
        :param input_file_path: path to the file, that should be evaluated
        :return: bool; true = fake, false = real
        """
        pipe = pipeline("image-classification", model="umm-maybe/AI-image-detector")
        output = pipe(input_file_path)
        if output[0]["score"] > output[1]["score"]:
            return False
        else:
            return True

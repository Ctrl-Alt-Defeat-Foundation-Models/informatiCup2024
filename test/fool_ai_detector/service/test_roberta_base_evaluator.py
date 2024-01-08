import os

from fool_ai_detector.service.roberta_base_openai_evaluator import RobertaBaseEvaluator


class TestRobertaBaseEvaluator:
    TEST_TEXT = "Berlin, the capital of Germany, is a dynamic city that encapsulates both a rich history and a " \
                "vibrant contemporary culture. Its iconic Brandenburg Gate stands as a symbol of unity and " \
                "reconciliation, while the remnants of the Berlin Wall serve as a stark reminder of the city's " \
                "divided past. With a thriving arts scene, diverse culinary offerings, and a youthful energy, " \
                "Berlin is a city that constantly reinvents itself, making it a must-visit destination for travelers " \
                "seeking a blend of tradition and innovation."

    def set_up(self):
        """
        Helper method: This method creates the output test folder.
        """
        if os.path.exists("berlin.txt"):
            os.remove("berlin.txt")
        with open("berlin.txt", "w") as text_file:
            text_file.write(self.TEST_TEXT)

    def test_normal_evaluation(self):
        self.set_up()

        roberta_evaluator = RobertaBaseEvaluator()
        is_fake = roberta_evaluator.evaluate(os.path.join(".", "berlin.txt"))

        assert is_fake

        if os.path.exists(os.path.join(".", "berlin.txt")):
            os.remove(os.path.join(".", "berlin.txt"))

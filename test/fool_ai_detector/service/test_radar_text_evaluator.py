import os

from fool_ai_detector.service.radar_text_evaluator import RadarEvaluator


class TestRadarEvaluator:
    TEST_TEXT = "Berlin, the capital of Germany, is a dynamic city that encapsulates both a rich history and a " \
                "vibrant contemporary culture. Its iconic Brandenburg Gate stands as a symbol of unity and " \
                "reconciliation, while the remnants of the Berlin Wall serve as a stark reminder of the city's " \
                "divided past. With a thriving arts scene, diverse culinary offerings, and a youthful energy, " \
                "Berlin is a city that constantly reinvents itself, making it a must-visit destination for travelers " \
                "seeking a blend of tradition and innovation."
    TEST_FILE = "berlin.txt"

    def set_up(self):
        """
        Helper method: This method writes the test text into a file.
        """

        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)
        with open(self.TEST_FILE, "w") as text_file:
            text_file.write(self.TEST_TEXT)

    def test_normal_evaluation(self):
        self.set_up()

        radar_evaluator = RadarEvaluator()
        is_fake = radar_evaluator.evaluate(os.path.join(".", self.TEST_FILE))

        assert is_fake

        if os.path.exists(os.path.join(".", self.TEST_FILE)):
            os.remove(os.path.join(".", self.TEST_FILE))

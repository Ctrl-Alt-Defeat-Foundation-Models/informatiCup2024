import os

from fool_ai_detector.service.nahrawy_image_evaluator import NahrawyEvaluator


class TestNahrawyEvaluator:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_processor_file_path = os.path.join(base_path_this_class, '..', '..', '..', 'src',
                                              'fool_ai_detector', 'resources', 'ai_gen_images', 'clownfish.png')

    def test_nahrawy_evaluation(self):
        nahrawy_evaluator = NahrawyEvaluator()
        is_fake = nahrawy_evaluator.evaluate(self.output_processor_file_path)

        assert isinstance(is_fake, bool)

import os

from fool_ai_detector.service.umm_maybe_ai_image_evaluator import UmmMaybeEvaluator


class TestUmmMaybeEvaluator:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_processor_file_path = os.path.join(base_path_this_class, '..', '..', '..', 'src',
                                              'fool_ai_detector', 'resources', 'ai_gen_images', 'clownfish.png')

    def test_umm_maybe_evaluation(self):
        umm_maybe_evaluator = UmmMaybeEvaluator()
        is_fake = umm_maybe_evaluator.evaluate(self.output_processor_file_path)

        assert isinstance(is_fake, bool)

import os

from src.fool_ai_detector.service.resnet18_evaluator import Resnet18Evaluator


class TestResnet18Evaluator:
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    output_processor_file_path = os.path.join(base_path_this_class, '..', '..', '..', 'src',
                                              'fool_ai_detector', 'resources', 'ai_gen_images', 'clownfish.png')

    def test_normal_evaluation(self):

        resnet18_evaluator = Resnet18Evaluator()
        is_fake = resnet18_evaluator.evaluate(self.output_processor_file_path)

        assert isinstance(is_fake, bool)

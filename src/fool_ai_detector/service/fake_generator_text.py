from pathlib import Path
import os
import random

from fool_ai_detector.model.generator import Generator


class FakeGeneratorText(Generator):
    base_path_this_class = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_path_this_class, '..', 'resources', 'ai_gen_text')
    texts = []

    def __init__(self):
        for text in os.listdir(self.dir_path):
            if os.path.isfile(os.path.join(self.dir_path, text)):
                self.texts.append(os.path.join(self.dir_path, text))

    def generate(self, output_file_path):
        """
           Method that takes one random text of the ai_gen_text directory and puts it in another directory.
        """
        random_text_index = random.randint(0, len(self.texts) - 1)
        random_text_path = self.texts[random_text_index]
        random_text_name = os.path.basename(random_text_path)
        random_text = Path(random_text_path).read_text()
        if not os.path.exists(output_file_path):
            os.mkdir(output_file_path)
        Path(os.path.join(output_file_path, random_text_name)).write_text(random_text)



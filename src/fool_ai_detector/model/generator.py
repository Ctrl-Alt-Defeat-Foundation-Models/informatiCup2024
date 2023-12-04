"""
Abstract Base Class of a Generator
"""
from abc import ABC, abstractmethod


class Generator(ABC):
    """
    Abstract Base Class of a Generator

    This can be used as interface to abstract from different generating models
    """

    def __int__(self):
        self.type = "abstract"

    @abstractmethod
    def generate(self, output_file_path, prompt=""):
        """
        Generates an artefact and returns it
        :param output_file_path: Path, where the generated file should be written to
        :param prompt: Text (multiple words, sentences) defining the theme of the generated element
        """
        pass

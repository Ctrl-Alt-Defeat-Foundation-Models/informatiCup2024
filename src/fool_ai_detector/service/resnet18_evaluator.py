"""
Evaluator based on the AI-image-detector by kgmann

"""
from fool_ai_detector.model.evaluator import Evaluator
import timm
import torch
from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform


class Resnet18Evaluator(Evaluator):
    """
    Resnet-18 Evaluator
    """

    def evaluate(self, input_file_path) -> bool:
        """
        Evaluates a given image based on the specific detector
        :param input_file_path: path to the file, that should be evaluated
        :return: bool; true = fake, false = real
        """
        model = timm.create_model("hf_hub:kgmann/ai-image-det-resnet18", pretrained=True)

        # Set model to eval mode for inference
        model.eval()

        # Create Transform
        transform = create_transform(**resolve_data_config(model.pretrained_cfg, model=model))

        # Get the labels from the model config
        labels = model.pretrained_cfg['label_names']

        # Use your own image file here...
        image = Image.open(input_file_path).convert('RGB')

        # Process PIL image with transforms and add a batch dimension
        x = transform(image).unsqueeze(0)

        # Pass inputs to model forward function to get outputs
        out = model(x)

        # Apply softmax to get predicted probabilities for each class
        probabilities = torch.nn.functional.softmax(out[0], dim=0)

        # Grab the values and indices of top 5 predicted classes
        _, indices = torch.topk(probabilities, 1)

        if labels[indices[0].item()] == "NOT AI":
            return False
        else:
            return True

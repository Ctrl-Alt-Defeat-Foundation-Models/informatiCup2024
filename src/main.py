import typer
import os
import shutil
from typing import Optional
from typing_extensions import Annotated

from fool_ai_detector.service.fake_generator_text import FakeGeneratorText
from fool_ai_detector.service.gpt2_text_generator import GPT2TextGenerator
from fool_ai_detector.service.falcon_text_generator import FalconRW1BTextGenerator
from fool_ai_detector.service.fake_generator_image import FakeGeneratorImage
from fool_ai_detector.service.stable_diffusion_image_generator import StableDiffusionImageGenerator
from fool_ai_detector.service.dalle_image_generator import DalleImageGenerator
from fool_ai_detector.service.double_whitespace_processor_text import DoubleWhitespaceProcessor
from fool_ai_detector.service.typo_text_processor import TypoProcessor
from fool_ai_detector.service.translator_processor import TranslatorProcessor
from fool_ai_detector.service.gaussian_processor import GaussianProcessor
from fool_ai_detector.service.poisson_processor import PoissonProcessor
from fool_ai_detector.service.s_and_p_processor import SAndPProcessor
from fool_ai_detector.service.speckle_processor import SpeckleProcessor
from fool_ai_detector.service.roberta_base_openai_evaluator import RobertaBaseEvaluator
from fool_ai_detector.service.radar_text_evaluator import RadarEvaluator
from fool_ai_detector.service.umm_maybe_ai_image_evaluator import UmmMaybeEvaluator
from fool_ai_detector.service.nahrawy_image_evaluator import NahrawyEvaluator
from fool_ai_detector.service.resnet18_evaluator import Resnet18Evaluator
from fool_ai_detector.service.csv_writer import CSVWriter

app = typer.Typer()


@app.command()
def generate(generator: str, output_file_path: str):
    match generator:
        case "fake_generator_text":
            typer.echo("Using fake_generator_text")
            generator_model = FakeGeneratorText()
        case "gpt2_generator_text":
            typer.echo("Using GPT2 text generator")
            generator_model = GPT2TextGenerator()
        case "falcon_generator_text":
            typer.echo("Using Falcon text generator")
            generator_model = FalconRW1BTextGenerator()
        case "fake_generator_image":
            typer.echo("Using fake_generator_image")
            generator_model = FakeGeneratorImage()
        case "stable_diffusion_generator_image":
            typer.echo("Using stable_diffusion_generator")
            generator_model = StableDiffusionImageGenerator()
        case "dallE_generator_image":
            typer.echo("Using DallE image generator")
            generator_model = DalleImageGenerator()
        case _:
            typer.secho("Error given generator not available", err=True, fg=typer.colors.RED)
            raise typer.Exit()
    generator_model.generate(output_file_path)


@app.command()
def process(input_file: str, output_file: str, processor: Annotated[Optional[str], typer.Option()] = None):
    if not os.path.isabs(input_file):
        input_file = os.path.join(os.getcwd(), "src", input_file)
    if not os.path.isabs(output_file):
        output_file = os.path.join(os.getcwd(), "src", output_file)
    if processor is None:
        if input_file.endswith('png') or input_file.endswith('jpg') or input_file.endswith('jpeg'):
            GaussianProcessor().process(input_file, output_file)
            SAndPProcessor().process(output_file, output_file)
        elif input_file.endswith('txt'):
            TypoProcessor().process(input_file, output_file)
        return
    processors = processor.split("-")
    shutil.copy(input_file, output_file)
    for current_processor in processors:
        match current_processor:
            case "double_whitespace_processor_text":
                typer.echo("Using double_whitespace_processor")
                processor_model = DoubleWhitespaceProcessor()
            case "typo_processor_text":
                typer.echo("Using typo_text_processor")
                processor_model = TypoProcessor()
            case "translator_processor_text":
                typer.echo("Using translator_processor")
                processor_model = TranslatorProcessor()
            case "gaussian_processor_image":
                typer.echo("Using gaussian_processor_image")
                processor_model = GaussianProcessor()
            case "poisson_processor_image":
                typer.echo("Using poisson_processor")
                processor_model = PoissonProcessor()
            case "s_and_p_processor_image":
                typer.echo("Using s&p_processor")
                processor_model = SAndPProcessor()
            case "speckle_processor_image":
                typer.echo("Using speckle_processor")
                processor_model = SpeckleProcessor()
            case _:
                typer.secho("Error given processor not available", err=True, fg=typer.colors.RED)
                raise typer.Exit()
        if ((input_file.endswith('png') or input_file.endswith('jpg') or input_file.endswith('jpeg'))
                and processor.endswith('image')) or (input_file.endswith('txt') and processor.endswith('text')):
            processor_model.process(output_file, output_file)
        else:
            typer.secho("The format of the file is not consistent with the format of the processor", err=True,
                        fg=typer.colors.RED)
            raise typer.Exit()


@app.command()
def evaluate(evaluator: str, input_file_path: str):
    match evaluator:
        case "roberta_evaluator_text":
            typer.echo("Using roberta_base_openai_evaluator")
            evaluator_model = RobertaBaseEvaluator()
        case "radar_evaluator_text":
            typer.echo("Using radar_evaluator")
            evaluator_model = RadarEvaluator()
        case "umm_maybe_evaluator_image":
            typer.echo("Using umm_maybe_base_evaluator")
            evaluator_model = UmmMaybeEvaluator()
        case "nahrawy_evaluator_image":
            typer.echo("Using nahrawy_evaluator")
            evaluator_model = NahrawyEvaluator()
        case "resnet18_evaluator_image":
            typer.echo("Using resnet18_evaluator")
            evaluator_model = Resnet18Evaluator()
        case _:
            typer.secho("Error given evaluator not available", err=True, fg=typer.colors.RED)
            raise typer.Exit()
    if ((input_file_path.endswith('png') or input_file_path.endswith('jpg') or input_file_path.endswith('jpeg')) and
            evaluator.endswith('image') or (input_file_path.endswith('txt') and evaluator.endswith('text'))):
        is_fake = evaluator_model.evaluate(input_file_path)
        if is_fake:
            typer.secho("---> This " + input_file_path[11:-4] + " is generated", fg=typer.colors.BRIGHT_GREEN,
                        bold=True)
            return True
        else:
            typer.secho("---> This " + input_file_path[11:-4] + " is not generated", fg=typer.colors.GREEN, bold=True)
            return False
    else:
        typer.secho("The format of the file is not consistent with the format of the evaluator", err=True,
                    fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def pipeline(generator: str, processor: str, evaluator: str,
             number_of_runthroughs: Optional[int] = typer.Argument(default=1)):
    content = generate_images_for_pipeline(generator, number_of_runthroughs)

    processors = processor.split("/")
    for current_processor in processors:
        process_for_pipeline(current_processor, content)

        evaluate_for_pipeline(evaluator, generator, current_processor, content, number_of_runthroughs)


def evaluate_for_pipeline(evaluator, generator, processor, images, number_of_runthroughs_param):
    """
    This method evaluates for every evaluator the original and the processed kind of image
    :param evaluator: all evaluators seperated with "-"
    :param generator: generator used
    :param processor: all processor seperated with "-"
    :param images: images generated as list of tuples (index_0 = unprocessed, index_1 = processed)
    :param number_of_runthroughs_param: number of images generated for this run
    """
    text_or_image = "image" if generator.endswith("image") else "text"
    evaluators = evaluator.split("-")
    for current_evaluator in evaluators:
        number_of_detections_before_process = 0
        number_of_detections_after_process = 0
        csv_writer = CSVWriter(generator, processor, current_evaluator, text_or_image, number_of_runthroughs_param)
        for image in images:
            is_original_ai = evaluate(current_evaluator, image[0])
            is_processed_ai = evaluate(current_evaluator, image[1])

            if is_original_ai and is_processed_ai:
                number_of_detections_before_process += 1
                number_of_detections_after_process += 1
                csv_writer.increase_ai_ai()
            elif not is_original_ai and not is_processed_ai:
                csv_writer.increase_human_human()
            elif not is_original_ai and is_processed_ai:
                number_of_detections_after_process += 1
                csv_writer.increase_human_ai()
            elif is_original_ai and not is_processed_ai:
                number_of_detections_before_process += 1
                csv_writer.increase_ai_human()

        csv_writer.write_to_csv()
        typer.secho(
            current_evaluator + ": Before processing: " + str(number_of_detections_before_process) + " out of " +
            str(number_of_runthroughs_param) + " were detected as generated.", fg=typer.colors.CYAN)
        typer.secho(
            current_evaluator + ": After processing: " + str(number_of_detections_after_process) + " out of " +
            str(number_of_runthroughs_param) + " were detected as generated.", fg=typer.colors.CYAN)


def process_for_pipeline(processor, content_param):
    """
    This Method processes all content
    :param processor: all processors the author wants combined with "-"
    :param content_param: all content as Tuples, (index_0 = unprocessed, index_1 = processed)
    """
    for content in content_param:
        process(processor, content[0], content[1])


def generate_images_for_pipeline(generator, number_of_runthroughs_param):
    """
    This method generates number_of_runthroughs images and saves them in the output folder
    :param generator: generator that has to be used
    :param number_of_runthroughs_param: number of images to generate
    :return: list of images
    """

    if not os.path.exists('src/output'):
        os.makedirs('src/output')
    if generator.endswith('text'):
        first_file = "src/output/original_text.txt"
        second_file = "src/output/augmented_text.txt"
    else:
        first_file = "src/output/original_image.png"
        second_file = "src/output/augmented_image.png"

    ret_images = []
    first_file_start = first_file.split(".")[0]
    first_file_end = first_file.split(".")[1]
    second_file_start = second_file.split(".")[0]
    second_file_end = second_file.split(".")[1]
    while number_of_runthroughs_param > 0:
        first_file = first_file_start + str(number_of_runthroughs_param) + "." + first_file_end

        second_file = second_file_start + str(number_of_runthroughs_param) + "." + second_file_end

        try:
            generate(generator, first_file)
            shutil.copy(first_file, second_file)
            ret_images.append((first_file, second_file))
            number_of_runthroughs_param -= 1
        except UnicodeEncodeError:
            print("UnicodeEncodeError, ignore this run!")

    return ret_images


if __name__ == "__main__":
    app()

import typer
import os
from typing import Optional
from fool_ai_detector.service.fake_generator_image import FakeGeneratorImage
from fool_ai_detector.service.fake_generator_text import FakeGeneratorText
from fool_ai_detector.service.naive_baseline_processor_image import NaiveBaselineProcessorImage
from fool_ai_detector.service.naive_baseline_processor_text import NaiveBaselineProcessorText
from fool_ai_detector.service.roberta_base_openai_evaluator import RobertaBaseEvaluator
from fool_ai_detector.service.translator_processor import TranslatorProcessor
from fool_ai_detector.service.umm_maybe_ai_image_evaluator import UmmMaybeEvaluator
from fool_ai_detector.service.stable_diffusion_image_generator import StableDiffusionImageGenerator
from fool_ai_detector.service.gpt2_text_generator import GPT2TextGenerator

app = typer.Typer()


@app.command()
def generate(generator: str, output_file_path: str):
    match generator:
        case "fake_generator_text":
            typer.echo("Using fake_generator_text")
            generator_model = FakeGeneratorText()
        case "fake_generator_image":
            typer.echo("Using fake_generator_image")
            generator_model = FakeGeneratorImage()
        case ("stable_diffusion_generator_image"):
            typer.echo("Using stable_diffusion_generator")
            generator_model = StableDiffusionImageGenerator()
        case("gpt2_generator_text"):
            typer.echo("Using GPT2 text generator")
            generator_model = GPT2TextGenerator()
        case _:
            typer.secho("Error given generator not available", err=True, fg=typer.colors.RED)
            raise typer.Exit()
    generator_model.generate(output_file_path)


@app.command()
def process(processor: str, input_file: str, output_file: str):
    match processor:
        case "naive_processor_image":
            typer.echo("Using naive_baseline_processor_image")
            processor_model = NaiveBaselineProcessorImage()
        case "naive_processor_text":
            typer.echo("Using naive_baseline_processor_text")
            processor_model = NaiveBaselineProcessorText()
        case "translator_processor_text":
            typer.echo("Using translator_processor")
            processor_model = TranslatorProcessor()
        case _:
            typer.secho("Error given processor not available", err=True, fg=typer.colors.RED)
            raise typer.Exit()
    if output_file.endswith('png') or output_file.endswith('jpg') or output_file.endswith('jpeg') and processor.endswith('image'):
        processor_model.process(input_file, output_file)
    elif output_file.endswith('txt') and processor.endswith('text'):
        processor_model.process(input_file, output_file)
    else:
        typer.secho("The format of the file is not consistent with the format of the processor", err=True, fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def evaluate(evaluator: str, input_file_path: str):
    match evaluator:
        case "roberta_evaluator_text":
            typer.echo("Using roberta_base_openai_evaluator")
            evaluator_model = RobertaBaseEvaluator()
        case "umm_maybe_evaluator_image":
            typer.echo("Using umm_maybe_base_evaluator")
            evaluator_model = UmmMaybeEvaluator()
        case _:
            typer.secho("Error given evaluator not available", err=True, fg=typer.colors.RED)
            raise typer.Exit()
    if input_file_path.endswith('png') or input_file_path.endswith('jpg') or input_file_path.endswith('jpeg') and evaluator.endswith('image'):
        is_fake = evaluator_model.evaluate(input_file_path)
        if is_fake:
            typer.secho("---> This " + input_file_path[11:-4] + " is generated", fg=typer.colors.BRIGHT_GREEN, bold=True)
            return True
        else:
            typer.secho("---> This " + input_file_path[11:-4] + " is not generated", fg=typer.colors.GREEN, bold=True)
            return False
    elif input_file_path.endswith('txt') and evaluator.endswith('text'):
        is_fake = evaluator_model.evaluate(input_file_path)
        if is_fake:
            typer.secho("---> This " + input_file_path[11:-4] + " is generated", fg=typer.colors.BRIGHT_GREEN, bold=True)
            return True
        else:
            typer.secho("---> This " + input_file_path[11:-4] + " is not generated", fg=typer.colors.GREEN, bold=True)
            return False
    else:
        typer.secho("The format of the file is not consistent with the format of the processor", err=True, fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def pipeline(generator: str, processor: str, evaluator: str, number_of_runthroughs: Optional[int] = typer.Argument(default=1)):
    original_number_of_runthroughs = number_of_runthroughs
    number_of_detections_before_process = 0
    number_of_detections_after_process = 0
    if not os.path.exists('src/output'):
        os.makedirs('src/output')
    if generator.endswith('text'):
        first_file = "src/output/original_text.txt"
        second_file = "src/output/augmented_text.txt"
    else:
        first_file = "src/output/original_image.png"
        second_file = "src/output/augmented_image.png"
    while number_of_runthroughs > 0:
        generate(generator, first_file)
        process(processor, first_file, second_file)
        if evaluate(evaluator, first_file):
            number_of_detections_before_process += 1
        if evaluate(evaluator, second_file):
            number_of_detections_after_process += 1
        number_of_runthroughs -= 1
    typer.secho("Before processing: " + str(number_of_detections_before_process) + " out of " + str(original_number_of_runthroughs) + " were detected as generated.", fg=typer.colors.CYAN)
    typer.secho("After processing: " + str(number_of_detections_after_process) + " out of " + str(original_number_of_runthroughs) + " were detected as generated.", fg=typer.colors.CYAN)


if __name__ == "__main__":
    app()

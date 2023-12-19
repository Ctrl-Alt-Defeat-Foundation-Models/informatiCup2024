import typer
import os
from fool_ai_detector.service.fake_generator_image import FakeGeneratorImage
from fool_ai_detector.service.fake_generator_text import FakeGeneratorText
from fool_ai_detector.service.naive_baseline_processor_image import NaiveBaselineProcessorImage
from fool_ai_detector.service.naive_baseline_processor_text import NaiveBaselineProcessorText
from fool_ai_detector.service.roberta_base_openai_evaluator import RobertaBaseEvaluator
from fool_ai_detector.service.umm_maybe_ai_image_evaluator import UmmMaybeEvaluator
from fool_ai_detector.service.stable_diffusion_image_generator import StableDiffusionImageGenerator
from fool_ai_detector.service.gpt2_text_generator import GPT2TextGenerator
from fool_ai_detector.service.poisson_processor import PoissonProcessor

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
        case "poisson_processor_image":
            typer.echo("Using poisson_processor")
            processor_model = PoissonProcessor()
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
            typer.secho("---> This image is generated", fg=typer.colors.BRIGHT_GREEN, bold=True)
        else:
            typer.secho("---> This image is not generated", fg=typer.colors.GREEN, bold=True)
    elif input_file_path.endswith('txt') and evaluator.endswith('text'):
        is_fake = evaluator_model.evaluate(input_file_path)
        if is_fake:
            typer.secho("---> This text is generated", fg=typer.colors.BRIGHT_GREEN, bold=True)
        else:
            typer.secho("---> This text is not generated", fg=typer.colors.GREEN, bold=True)
    else:
        typer.secho("The format of the file is not consistent with the format of the processor", err=True, fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def pipeline(generator: str, processor: str, evaluator: str):
    if not os.path.exists('src/output'):
        os.makedirs('src/output')
    if generator.endswith('text'):
        first_file = "src/output/original_text.txt"
        second_file = "src/output/augmented_text.txt"
    else:
        first_file = "src/output/original_image.png"
        second_file = "src/output/augmented_image.png"
    generate(generator, first_file)
    process(processor, first_file, second_file)
    evaluate(evaluator, first_file)
    evaluate(evaluator, second_file)


if __name__ == "__main__":
    app()

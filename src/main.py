import typer
from fool_ai_detector.model.generator import Generator
from fool_ai_detector.service.fake_generator_image import FakeGeneratorImage
from fool_ai_detector.service.fake_generator_text import FakeGeneratorText
from fool_ai_detector.model.processor import Processor
from fool_ai_detector.service.naive_baseline_processor_image import NaiveBaselineProcessorImage
from fool_ai_detector.model.evaluator import Evaluator
from fool_ai_detector.service.roberta_base_openai_evaluator import RobertaBaseEvaluator

app = typer.Typer()


@app.command()
def generate(generator: str, output_file_path: str):
    generator_model = None
    match generator:
        case "fake_generator_text":
            typer.echo("Using fake_generator_text")
            generator_model = FakeGeneratorText
        case "fake_generator_image":
            typer.echo("Using fake_generator_image")
            generator_model = FakeGeneratorImage
        case _:
            typer.echo("Error given generator not available", err=True)
    generator_model.generate(output_file_path)


@app.command()
def process(processor: str, input_file: str, output_file: str):
    processor_model = None
    match processor:
        case "naive_baseline_processor":
            typer.echo("naive_baseline_processor")
            processor_model = NaiveBaselineProcessorImage
        case _:
            typer.echo("Error given processor not available", err=True)
    processor_model.process(input_file, output_file)


@app.command()
def evaluate(evaluator: str, input_file_path: str):
    evaluator_model = None
    match evaluator:
        case "roberta_base_openai_evaluator":
            typer.echo("roberta_base_openai_evaluator")
            evaluator_model = RobertaBaseEvaluator
        case _:
            typer.echo("Error given evaluator not available", err=True)
    evaluator_model.evaluate(input_file_path)


@app.command()
def pipeline(generator: str, processor: str, evaluator: str, output_generator: str, output_evaluator: str):
    input_for_process = generate(generator, output_generator)
    input_for_evaluator = process(processor, input_for_process, output_evaluator)
    evaluate(evaluator, input_for_evaluator)
    typer.echo("Error given parameters not available", err=True)


if __name__ == "__main__":
    app()

import typer
from fool_ai_detector.service.fake_generator_image import FakeGeneratorImage
from fool_ai_detector.service.fake_generator_text import FakeGeneratorText
from fool_ai_detector.service.naive_baseline_processor_image import NaiveBaselineProcessorImage
from fool_ai_detector.service.naive_baseline_processor_text import NaiveBaselineProcessorText
from fool_ai_detector.service.roberta_base_openai_evaluator import RobertaBaseEvaluator

app = typer.Typer()


@app.command()
def generate(generator: str, output_file_path: str):
    generator_model = None
    match generator:
        case "fake_generator_text":
            typer.echo("Using fake_generator_text")
            generator_model = FakeGeneratorText()
        case "fake_generator_image":
            typer.echo("Using fake_generator_image")
            generator_model = FakeGeneratorImage()
        case _:
            typer.echo("Error given generator not available", err=True)
    generator_model.generate(output_file_path)


@app.command()
def process(processor: str, input_file: str, output_file: str):
    processor_model = None
    match processor:
        case "naive_baseline_processor_image":
            typer.echo("Using naive_baseline_processor_image")
            processor_model = NaiveBaselineProcessorImage()
        case "naive_baseline_processor_text":
            typer.echo("Using naive_baseline_processor_text")
            processor_model = NaiveBaselineProcessorText()
        case _:
            typer.echo("Error given processor not available", err=True)
    processor_model.process(input_file, output_file)


@app.command()
def evaluate(evaluator: str, input_file_path: str):
    evaluator_model = None
    match evaluator:
        case "roberta_base_openai_evaluator":
            typer.echo("roberta_base_openai_evaluator")
            evaluator_model = RobertaBaseEvaluator()
        case _:
            typer.echo("Error given evaluator not available", err=True)
    is_fake = evaluator_model.evaluate(input_file_path)
    if is_fake:
        typer.echo("This text is generated")
    else:
        typer.echo("This text is not generated")


@app.command()
def pipeline(generator: str, processor: str, evaluator: str):
    first_file = "test.txt"
    second_file = "test2.txt"
    generate(generator, first_file)
    process(processor, first_file, second_file)
    evaluate(evaluator, second_file)


if __name__ == "__main__":
    app()

import typer

app = typer.Typer()


@app.command()
def generate(generator: str, output_file_path: str):
    typer.echo("Error given generator not available", err=True)


@app.command()
def process(processor: str, input_file: str, output_file: str):
    typer.echo("Error given processor not available", err=True)


@app.command()
def evaluate(evaluator: str, input_file_path: str):
    typer.echo("Error given evaluator not available", err=True)


if __name__ == "__main__":
    app()

import typer

app = typer.Typer()


@app.command()
def generate():
    print("generating")


@app.command()
def process():
    print("processing")


@app.command()
def evaluate():
    print("evaluating")


if __name__ == "__main__":
    app()

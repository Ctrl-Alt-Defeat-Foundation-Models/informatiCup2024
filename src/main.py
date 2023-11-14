import typer

app = typer.Typer()

@app.command()
def generate():
    print("generating")

@app.command()
def augmentate():
    print("augmentating")

@app.command()
def evaluate():
    print("evaluating")

if __name__ == "__main__":
    app()

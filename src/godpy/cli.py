"""Console script for godpy."""
import godpy

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for godpy."""
    console.print("Replace this message by putting your code into "
               "godpy.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()

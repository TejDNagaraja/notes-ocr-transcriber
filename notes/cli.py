"""This module provides the Notes OCR Transcriber CLI."""
# notes/cli.py


from typing import Optional
from pathlib import Path
import typer
from notes import ERRORS, __app_name__, __version__, transcriber

app = typer.Typer()

@app.command()
def transcribe(
	image_path: str = typer.Option(
		"",
		"--image",
		"-i",
		prompt="Please enter a path to the notes image to transcribe."
	),
	output_dir_path: str = typer.Option(
		"",
		"--output-directory",
		"-o",
		prompt="Please enter a path to a directory to save the transcribed text file."
	)
) -> None:
	"""Transcribe image and write to a file in the output directory."""
	error = transcriber.transcribe(image_path, output_dir_path)
	if error:
		typer.secho(f'Transcription failed with "{ERRORS[error]}"')
		raise typer.Exit(1)
	else:
		typer.secho("Success")

def _version_callback(displayVersion: bool) -> None:
    if displayVersion:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Display app version.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
from pathlib import Path
from typing import Annotated, Optional

import typer

from md_to_pdf.converter import check_dependencies, convert

app = typer.Typer(
    name="md-to-pdf",
    help="Convert Markdown documents to styled PDFs.",
    add_completion=False,
)


@app.command()
def main(
    input_file: Annotated[
        Path,
        typer.Argument(help="Path to the Markdown file to convert."),
    ],
    output: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Output PDF path. Defaults to <input>.pdf."),
    ] = None,
    css: Annotated[
        Optional[Path],
        typer.Option("--css", help="CSS stylesheet. Names are resolved from md_to_pdf/styles/ first."),
    ] = None,
    syntax_highlighting: Annotated[
        str,
        typer.Option("--syntax-highlighting", help="Pandoc syntax highlight theme."),
    ] = "tango",
) -> None:
    """Convert a Markdown file to a styled PDF."""
    check_dependencies()

    output_file = output or input_file.with_suffix(".pdf")

    print(f"Converting {input_file} -> {output_file}")
    convert(input_file, output_file, css_file=css, syntax_highlighting=syntax_highlighting)
    print(f"Done! Output: {output_file}")

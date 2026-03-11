from pathlib import Path
import shutil
import subprocess
import sys

import pypandoc


STYLES_DIR = Path(__file__).parent / "styles"
DEFAULT_CSS = STYLES_DIR / "default.css"


def check_dependencies() -> None:
    """Verify that Pandoc and WeasyPrint are installed and accessible."""
    if not shutil.which("pandoc"):
        print("Error: Pandoc is not installed or not on PATH.", file=sys.stderr)
        print("  Install with: brew install pandoc", file=sys.stderr)
        raise SystemExit(1)

    if not shutil.which("weasyprint"):
        print("Error: WeasyPrint is not installed or not on PATH.", file=sys.stderr)
        print("  Install with: brew install weasyprint", file=sys.stderr)
        raise SystemExit(1)


def convert(
    input_file: Path,
    output_file: Path,
    css_file: Path | None = None,
    syntax_highlighting: str = "tango",
) -> Path:
    """Convert a Markdown file to PDF via Pandoc + WeasyPrint.

    Returns the output file path on success.
    """
    if css_file is None:
        css = DEFAULT_CSS
    elif not css_file.is_absolute() and not css_file.exists():
        css = STYLES_DIR / css_file
    else:
        css = css_file

    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}", file=sys.stderr)
        raise SystemExit(1)

    if not css.exists():
        print(f"Error: CSS file not found: {css}", file=sys.stderr)
        if css_file and not css_file.is_absolute():
            print(f"  Looked in: {css_file} and {STYLES_DIR / css_file}", file=sys.stderr)
        raise SystemExit(1)

    extra_args = [
        "--pdf-engine=weasyprint",
        f"--css={css}",
        f"--syntax-highlighting={syntax_highlighting}",
        "--standalone",
        f"--resource-path={input_file.parent}",
    ]

    try:
        pypandoc.convert_file(
            str(input_file),
            "pdf",
            outputfile=str(output_file),
            extra_args=extra_args,
        )
    except subprocess.CalledProcessError as exc:
        print(f"Error: Pandoc conversion failed:\n{exc.stderr}", file=sys.stderr)
        raise SystemExit(1)
    except Exception as exc:
        print(f"Error: Conversion failed: {exc}", file=sys.stderr)
        raise SystemExit(1)

    return output_file

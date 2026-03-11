# md-to-pdf

A Python console application that converts Markdown documents to styled PDFs using Pandoc and WeasyPrint.

## Features

- Markdown to PDF conversion with CSS-based styling
- Syntax-highlighted code blocks
- Table support with styled borders and alternating rows
- Embedded image support
- Bundled default stylesheet with professional look
- Custom CSS override via `--css` flag

## Prerequisites

**Python 3.10+** is required.

### System Dependencies

Install Pandoc and WeasyPrint via Homebrew (macOS):

```bash
brew install pandoc weasyprint
```

### Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Basic — outputs <filename>.pdf in the same directory
python -m md_to_pdf document.md

# Specify output file
python -m md_to_pdf document.md -o output.pdf

# Use a custom CSS stylesheet
python -m md_to_pdf document.md --css my-style.css

# Change syntax highlight theme (default: tango)
python -m md_to_pdf document.md --syntax-highlighting monokai
```

## Custom Styling

The `--css` flag resolves names relative to the bundled `md_to_pdf/styles/` directory, so you can reference built-in stylesheets by filename alone:

```bash
# Uses md_to_pdf/styles/resume.css
python -m md_to_pdf converted/resume.md -o resume.pdf --css resume.css
```

You can also pass a full relative or absolute path to use your own CSS from anywhere:

```bash
cp md_to_pdf/styles/default.css my-custom-style.css
# ... edit my-custom-style.css ...
python -m md_to_pdf document.md --css ./my-custom-style.css
```

The CSS uses `@page` rules for print layout (margins, page size) and standard CSS for typography, tables, code blocks, and images.

## License

MIT

## Acknowledgments

- [Pandoc](https://pandoc.org/)
- [WeasyPrint](https://weasyprint.org/)
- [typer](https://typer.tiangolo.com/)

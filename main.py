#!/usr/bin/env python
# -*- coding: utf-8 -*-

from note_generator import NoteGenerator
import typer

app = typer.Typer()

@app.command()
def extract_notes(
    pdf_path: str = typer.Option(..., "--pdf_path", help="Path to the PDF file"),
    page_start: int = typer.Option(..., "--page_start", help="Starting page number"),
    page_end: int = typer.Option(..., "--page_end", help="Ending page number"),
    chunk_size: int = typer.Option(..., "--chunk_size", help="size in characters to chunk the pdf into")
):
    """
    Extracts notes from a specified range of pages in a PDF.
    """
    #  typer.echo(f"Extracting text from {pdf_path}, pages {page_start} to {page_end}")
    ng = NoteGenerator(pdf_path)
    print(ng.process_text(start_page= page_start, end_page = page_end, chunk_size=chunk_size))

if __name__ == "__main__":
    app()


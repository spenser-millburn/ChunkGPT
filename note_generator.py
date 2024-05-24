#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileReader
from IPython.display import Markdown
import pyperclip as pc
from text_generation import TextGeneration
from tqdm import tqdm


class NoteGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tg = TextGeneration()

    def get_text_pdf(self, start_page, end_page):
        with open(self.file_path, 'rb') as f:
            reader = PdfFileReader(f)
            text = ""
            for i in range(start_page, end_page + 1):
                text += reader.getPage(i).extractText()
        return text

    @staticmethod
    def chunk_string(string, n):
        return [string[i:i + n] for i in range(0, len(string), n)]

    def process_pdf(self, start_page, end_page, chunk_size, process_chunk, join_with):
        text = self.get_text_pdf(start_page, end_page)
        chunked_string = self.chunk_string(text, chunk_size)
        notes = []

        for i, chunk in enumerate(tqdm(chunked_string, desc="Processing chunks", unit="chunk")):
            processed_chunk = process_chunk(chunk)
            notes.append(processed_chunk + "\n\n")

        formatted_notes = join_with.join(notes)
        return formatted_notes

    def process_text(self, start_page, end_page, chunk_size):
        def process_chunk(chunk):
            one_line_summary_prompt = ("Please provide markdown notes (use only h4 for headings) for only "
                                       "the most important concepts here no extra stuff. Use katex inline "
                                       "blocks (surrounded by $ for Jupyter)")
            return self.tg.generate_text(one_line_summary_prompt + chunk)

        return self.process_pdf(start_page, end_page, chunk_size, process_chunk, "")

    def solve_problems(self, start_page, end_page, chunk_size):
        def process_chunk(chunk):
            solve_prompt = ("Please solve each of these problems with python, making sure to print documentation "
                            "with markdown (this will be displayed in a Jupyter notebook). "
                            "Use katex blocks and/or sympy when necessary ( ensure that the blocks are surrounded by $ for Jupyter and not \[ or \])")
            return self.tg.generate_text(solve_prompt + chunk)

        return self.process_pdf(start_page, end_page, chunk_size, process_chunk, "\n\n\n")



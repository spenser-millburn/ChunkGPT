#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileReader
from IPython.display import Markdown
import pyperclip as pc
from text_generation import TextGeneration


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

    def process_text(self, start_page, end_page, chunk_size):
        text = self.get_text_pdf(start_page, end_page)
        chunked_string = self.chunk_string(text, chunk_size)
        notes = []
        
        for chunk in chunked_string:
            one_line_summary_prompt = ("Please provide markdown notes (use only h4 for headings) for only "
                                       "the most important concepts here no extra stuff. Use katex inline "
                                       "blocks (surrounded by $ for Jupyter)")
            one_line_summary = self.tg.generate_text(one_line_summary_prompt + chunk)
            notes.append(one_line_summary)
        
        formatted_notes = "".join(notes)
        return formatted_notes



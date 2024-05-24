# ChunkGPT

ChunkGPT is a Python application that chunk documents (currently limited to PDFs) into manageable sections and utilizes OpenAI's large language models to summarize the text. It's designed for anyone needing to quickly extract and comprehend the main points from extensive PDF documents.

## Features

- **PDF Chunking**: Breaks PDF documents into smaller sections for easier handling.
- **Text Summarization**: Uses OpenAI's language models to provide summaries of each chunk.
- **Clipboard Integration**: Summaries can be automatically copied to the clipboard for easy sharing and use.

## Requirements

- Python 3.x
- Typer
- OpenAI
- Pyperclip

## Installation

First, clone the repository to your local machine:

    git clone git@github.com:spenser-millburn/ChunkGPT.git
    cd ChunkGPT

install the required packages:

    pip install typer openai pyperclip

## Usage

To run the application, use the following command format:

    python3 main.py --pdf_path PATH_TO_PDF --page_start START_PAGE --page_end END_PAGE --chunk_size CHUNK_SIZE

### Parameters:

- `--pdf_path`: Path to the PDF file.
- `--page_start`: The starting page number for chunking.
- `--page_end`: The ending page number for chunking.
- `--chunk_size`: The number of characters per chunk.

Example:

    python3 main.py --pdf_path $DOWNLOADS/your_document.pdf --page_start 1 --page_end 4 --chunk_size 1000

## Output

The application outputs summaries directly to the console and copies them to your clipboard.

## Contributing

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is open-sourced under the MIT License.

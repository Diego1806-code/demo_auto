import pymupdf4llm
import pathlib

pathlib.Path("output.md").write_bytes(md_text.encode)
llama_reader = pymupdf4llm.LlamaMarkdownReader()
llama_docs = llama_reader.load_data("testpdf.pdf")
import pymupdf as fitz
import json 
import pandas as pd
import os
import sys


pdf_template_path = ".\testpdf.pdf"



def fill_pdf_with_mapping(pdf_template_path, mapping_json_path, output_pdf_path):
    with open(mapping_json_path, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    doc = fitz.open(pdf_template_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        for field, value in mapping.items():
            text_instances = page.search_for(field)
            for inst in text_instances:
                page.draw_rect(inst, color=(1, 1, 1), fill=(1, 1, 1))
                page.insert_text(
                    inst.tl,  
                    str(value),
                    fontsize=12,
                    color=(0, 0, 0)
                )

    doc.save(output_pdf_path)
    doc.close()
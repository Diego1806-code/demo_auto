import pymupdf as fitz
import json 
import pandas as pd
import os
import sys



def fill_pdf_with_mapping(pdf_template_path, mapping_json_path, output_pdf_path):
    # Load mapping from JSON
    with open(mapping_json_path, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    # Open the PDF template
    doc = fitz.open(pdf_template_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        for field, value in mapping.items():
            # Search for the field name in the PDF
            text_instances = page.search_for(field)
            for inst in text_instances:
                # Draw a white rectangle over the field name
                page.draw_rect(inst, color=(1, 1, 1), fill=(1, 1, 1))
                # Insert the mapped value
                page.insert_text(
                    inst.tl,  # top-left of the found field
                    str(value),
                    fontsize=12,
                    color=(0, 0, 0)
                )

    # Save the filled PDF
    doc.save(output_pdf_path)
    doc.close()
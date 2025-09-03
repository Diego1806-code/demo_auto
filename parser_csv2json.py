import csv
import json
import pandas as pd
import pymupdf as fitz

def parse_csv_to_json(pdf_source, csv_source):
    # Read the AI mapping
    try:
        with open('ai_mapping.json', 'r', encoding='utf-8') as mapping_file:
            field_mapping = json.load(mapping_file)['fields']
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        print("Warning: No valid AI mapping found, using default mapping")
        field_mapping = {}

    # Convert CSV to JSON as before
    df = pd.read_csv(csv_source, encoding='utf-8')
    df.to_json('data.json', orient='records', force_ascii=False, indent=4)

    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Use AI mapping to create data entry dictionary
    data_entry_data = {}
    first_row = data[0]  # Get first row of CSV data

    with fitz.open(pdf_source) as doc:
        target_page = doc[0]
        font_rgb = (0, 137, 210)
        font_color = tuple(value / 255 for value in font_rgb)

        for field in target_page.widgets():
            field_name = field.field_name
            # If we have an AI mapping for this field, use it
            if field_name in field_mapping and field_mapping[field_name]:
                csv_column = field_mapping[field_name]
                if csv_column in first_row:
                    if field.field_type == fitz.PDF_WIDGET_TYPE_TEXT:
                        field.field_value = str(first_row[csv_column])
                        field.update()
                    elif field.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
                        field.field_value = bool(first_row[csv_column])
                        field.update()

        doc.save("output.pdf")
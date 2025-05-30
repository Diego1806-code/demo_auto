import csv
import json
import pandas as pd
import pymupdf as fitz

def parse_csv_to_json(pdf_source, csv_source):
    with open(csv_source, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

    # converting csv to json
    df = pd.read_csv(csv_source, encoding='utf-8')
    df.to_json('data.json', orient='records', force_ascii=False, indent=4)

    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        print(data)

    # giving entry data
    data_entry_data = {
        "0" : data[0]["name"],
        "1" : data[0]["vorname"]
    }

    output = "output.pdf"

    with fitz.open(pdf_source) as doc:
        target_page = doc[0]
        font_rgb = (0, 137, 210)
        font_color = tuple(value / 255 for value in font_rgb)

        for indx, field in enumerate(target_page.widgets()):
            if field.field_type == fitz.PDF_WIDGET_TYPE_TEXT:
                field.field_value = str(data_entry_data.get(str(indx), ""))
                field.update()
            elif field.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
                field.field_value = data_entry_data.get(str(indx))
                field.update()
                target_page.insert_text(field.rect.tl, "This is index: {0}", format(indx), fontsize=12, color=font_color)

            if indx == len(data_entry_data.values()) - 1:
                break

        doc.save(output)
import pymupdf as fitz
import select_csv
import select_pdf
import filecheck
import csv
import json
import pandas as pd
import parser_csv2json as parser
import GUI

# TODO: add an excel option with GUI

GUI.run_gui()

filecheck.check_json()
filecheck.check_pdf()

pdf_source = select_pdf.select_pdf()
csv_source = select_csv.select_csv()

print(pdf_source)
print(csv_source)

parser.parse_csv_to_json(pdf_source, csv_source)
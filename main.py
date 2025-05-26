import pymupdf as fitz
import select_csv
import select_pdf
import parser_csv2json
import filecheck

filecheck.check_json()
filecheck.check_pdf()

pdf_source = select_pdf.select_pdf()
csv_source = select_csv.select_csv()

print(pdf_source)
print(csv_source)
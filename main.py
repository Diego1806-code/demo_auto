import pymupdf as fitz
import select_csv
import select_pdf
import parser_csv2json
import filecheck
import csv
import json
import pandas as pd

filecheck.check_json()
filecheck.check_pdf()

pdf_source = select_pdf.select_pdf()
csv_source = select_csv.select_csv()

print(pdf_source)
print(csv_source)


# opening csv file and reading it

with open(csv_source, 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# converting csv to json
df = pd.read_csv(csv_source, encoding='utf-8')
df.to_json('data.json', orient='records', force_ascii=False, indent=4)


with open('data.json', 'r', encoding='utf-8') as json_file:
    data = [json.loads(line) for line in json_file]
    print(data)

# giving entry data

data_entry_data = {
    "0" : data[0]["entry_data"],
}

output = "output.pdf"

with fitz.open(pdf_source) as doc:
    target_page = doc[0]  # Assuming you want to write on the first page
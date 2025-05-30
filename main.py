import pymupdf as fitz
import select_csv
import select_pdf
import filecheck
import csv
import json
import pandas as pd
import tkinter as tk
import parser_csv2json as parser


# TODO: add an excel option with GUI

root = tk.Tk()

root.geometry("300x200")
root.title("slect files")

#first button to select pdf file

PDF_button = tk.Button(root,
                   text="Select PDF",
                   command=select_pdf.select_pdf
                   )
PDF_button.pack(padx=20, pady=20, side=tk.TOP)

#button2 to select csv file

CSV_button = tk.Button(root,
                   text="Select CSV",
                   command=select_csv.select_csv
                   )
CSV_button.pack(padx=20, pady=20, side=tk.TOP)

#exit button

cancel = tk.Button(root,
                   text="Exit",
                   command=exit
                   )
cancel.pack(padx=20, pady=20, side=tk.BOTTOM)

root.mainloop()

filecheck.check_json()
filecheck.check_pdf()

pdf_source = select_pdf.select_pdf()
csv_source = select_csv.select_csv()

print(pdf_source)
print(csv_source)

parser.parse_csv_to_json(pdf_source, csv_source)
import select_pdf
import filecheck
import parser_csv2json as parser
import GUI
import localAI as AI

AI.getresponse()

filecheck.check_json()
filecheck.check_pdf()

pdf_source, csv_source = GUI.run_gui()

#pdf_source = select_pdf.select_pdf()
#csv_source = select_csv.select_csv()

print(select_pdf)
print(csv_source)

parser.parse_csv_to_json(pdf_source, csv_source)

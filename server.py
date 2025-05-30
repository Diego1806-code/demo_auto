from flask import Flask, request, render_template_string
import pandas as pd
import pymupdf as fitz
import ollama

app = Flask(__name__)

UPLOAD_FORM = """
<!doctype html>
<title>Upload PDF and CSV</title>
<h1>Upload PDF and CSV</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=pdf_file accept=".pdf" required>
  <input type=file name=csv_file accept=".csv" required>
  <input type=submit value=Upload>
</form>
{% if message %}
  <p>{{ message|safe }}</p>
{% endif %}
"""

def extract_pdf_fields(pdf_path):
    fields = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            for field in page.widgets():
                if field.field_name:
                    fields.append(field.field_name)
    return fields

def extract_csv_columns(csv_path):
    df = pd.read_csv(csv_path, nrows=1)
    return list(df.columns)

def ollama_field_mapping(pdf_fields, csv_columns):
    prompt = (
        f"Given these PDF fields: {pdf_fields}\n"
        f"And these CSV columns: {csv_columns}\n"
        "Suggest a JSON mapping where each PDF field is mapped to the most likely CSV column."
    )
    response = ollama.generate(
        model="llama3.2",  # or your preferred model
        prompt=prompt,
        stream=False
    )
    return response['response']

@app.route("/", methods=["GET", "POST"])
def upload():
    message = ""
    if request.method == "POST":
        pdf = request.files.get("pdf_file")
        csv = request.files.get("csv_file")
        if pdf and csv:
            pdf_path = f"./{pdf.filename}"
            csv_path = f"./{csv.filename}"
            pdf.save(pdf_path)
            csv.save(csv_path)
            pdf_fields = extract_pdf_fields(pdf_path)
            csv_columns = extract_csv_columns(csv_path)
            mapping = ollama_field_mapping(pdf_fields, csv_columns)
            message = f"Files uploaded!<br><b>AI Mapping Suggestion:</b><pre>{mapping}</pre>"
        else:
            message = "Please upload both files."
    return render_template_string(UPLOAD_FORM, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
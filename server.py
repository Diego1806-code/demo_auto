from flask import Flask, request, render_template_string
import pandas as pd
import pymupdf as fitz
import ollama
import json

app = Flask(__name__)

# ...existing code...
UPLOAD_FORM = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Upload PDF and CSV</title>
  <style>
    body {
      background: #f4f6fb;
      font-family: 'Segoe UI', Arial, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }
    .container {
      background: #fff;
      margin-top: 60px;
      padding: 32px 40px 24px 40px;
      border-radius: 12px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
      min-width: 340px;
      max-width: 90vw;
    }
    h1 {
      color: #2d3a4b;
      margin-bottom: 24px;
      font-size: 1.7em;
      text-align: center;
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    input[type="file"] {
      padding: 8px;
      border: 1px solid #cfd8dc;
      border-radius: 6px;
      background: #f9fafb;
      font-size: 1em;
    }
    input[type="submit"] {
      background: #1976d2;
      color: #fff;
      border: none;
      border-radius: 6px;
      padding: 12px;
      font-size: 1em;
      cursor: pointer;
      transition: background 0.2s;
    }
    input[type="submit"]:hover {
      background: #125ea7;
    }
    .message {
      margin-top: 18px;
      background: #e3f2fd;
      color: #0d47a1;
      border-left: 4px solid #1976d2;
      padding: 12px;
      border-radius: 6px;
      font-size: 1em;
      word-break: break-all;
    }
    pre {
      background: #f5f5f5;
      padding: 10px;
      border-radius: 6px;
      overflow-x: auto;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Upload PDF and CSV</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="pdf_file" accept=".pdf" required>
      <input type="file" name="csv_file" accept=".csv" required>
      <input type="submit" value="Upload">
    </form>
    {% if message %}
      <div class="message">{{ message|safe }}</div>
    {% endif %}
  </div>
</body>
</html>
"""
# ...existing code...

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
        "Suggest a JSON mapping where each PDF field is mapped to the most likely CSV column. DO ABSOLUTELY NOT RETURN ANYTHING EXCEPT FOR JSON!!!!!!!!!!! NO RESPONSE OR NOTING "
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
            with open("ai_mapping.json", "w", encoding="utf-8") as f:
              f.write(mapping if mapping.strip().startswith("{") else json.dumps(mapping))
        else:
            message = "Please upload both files."
    return render_template_string(UPLOAD_FORM, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



    
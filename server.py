from flask import Flask, request, render_template_string

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
  <p>{{ message }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def upload():
    message = ""
    if request.method == "POST":
        pdf = request.files.get("pdf_file")
        csv = request.files.get("csv_file")
        if pdf and csv:
            pdf.save(f"./{pdf.filename}")
            csv.save(f"./{csv.filename}")
            # Here you could call your AI logic or Ollama
            message = "Files uploaded!"
        else:
            message = "Please upload both files."
    return render_template_string(UPLOAD_FORM, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
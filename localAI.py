import ollama

def getresponse():
    prompt = (
        "You are an API. Only output valid JSON. "
        "Given the following PDF fields and CSV columns, return a JSON object mapping each PDF field to the most likely CSV column. "
        "Do not include any explanation or extra text, only output the JSON object. DO NOT GIVE ANYYYYYY ASUMPTOPNS NOT EVEN IN THE END OR ANYTHING!!!!!!!!!! "
        "PDF fields: [field1, field2]\nCSV columns: [col1, col2]"
    )
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response["message"]["content"])
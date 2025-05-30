import ollama

def tryout():
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": "hello"}])
    print(response["message"]["content"])
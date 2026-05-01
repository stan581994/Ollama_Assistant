import ollama

def chat(messages):
    response = ollama.chat(
        model = 'llama3',
        messages = messages,
        stream=True
    )
    return response
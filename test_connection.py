import ollama

try:
    print("Attempting to connect to Ollama...")
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': 'Why is the sky blue?'}]
    )
    print("Connection successful!")
    print("Response:", response['message']['content'])
except Exception as e:
    print(f"An error occurred: {e}")

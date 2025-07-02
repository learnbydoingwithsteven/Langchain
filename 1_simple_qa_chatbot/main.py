print("Script starting...")
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

print("Imports successful.")

# Load environment variables from .env
print("Loading .env file...")
load_dotenv()
print(".env file loaded.")

# Get the Ollama model from the environment variables
ollama_model = os.getenv("OLLAMA_MODEL")
print(f"OLLAMA_MODEL from .env: {ollama_model}")

if not ollama_model:
    print("Error: OLLAMA_MODEL not found in .env file. Please ensure the file exists and the variable is set.")
    exit()

# Initialize the Ollama LLM
print("Initializing Ollama LLM...")
llm = Ollama(model=ollama_model)
print("Ollama LLM initialized.")

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's questions."),
    ("user", "Question: {question}")
])

# Create a simple chain
chain = prompt | llm | StrOutputParser()

# Run the chatbot
if __name__ == "__main__":
    print("Simple Q&A Chatbot is running! Type 'exit' to quit.")
    try:
        while True:
            user_question = input("You: ")
            if user_question.lower() == 'exit':
                break
            response = chain.invoke({"question": user_question})
            print(f"Bot: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")


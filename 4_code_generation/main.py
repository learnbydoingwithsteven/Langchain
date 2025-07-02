import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv(dotenv_path='../.env')
ollama_model = os.getenv("OLLAMA_MODEL")

# Initialize Ollama LLM
llm = Ollama(model=ollama_model)

# Create a prompt template for code generation
prompt = ChatPromptTemplate.from_template(
    "Write a code snippet in {language} for the following task: {task}. "
    "Provide only the code, without any extra explanations or formatting."
)

# Create a simple chain
chain = prompt | llm | StrOutputParser()

# Run the code generator
if __name__ == "__main__":
    print("Code Generator is running! Type 'exit' to quit.")
    while True:
        language = input("Enter the programming language (e.g., Python): ")
        if language.lower() == 'exit':
            break
        task = input(f"Describe the code you want in {language}: ")
        if task.lower() == 'exit':
            break

        response = chain.invoke({"language": language, "task": task})
        print("\n--- Generated Code ---")
        print(response)
        print("----------------------\n")

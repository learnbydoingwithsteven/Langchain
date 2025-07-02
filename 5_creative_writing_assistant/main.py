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

# Create a prompt template for creative writing
prompt = ChatPromptTemplate.from_template(
    "Generate a short, creative story starter based on the following topic: {topic}."
)

# Create a simple chain
chain = prompt | llm | StrOutputParser()

# Run the creative writing assistant
if __name__ == "__main__":
    print("Creative Writing Assistant is running! Type 'exit' to quit.")
    while True:
        topic = input("Enter a topic for a story: ")
        if topic.lower() == 'exit':
            break

        response = chain.invoke({"topic": topic})
        print("\n--- Story Starter ---")
        print(response)
        print("---------------------\n")

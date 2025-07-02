import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import TextLoader

# Load environment variables from .env in the parent directory
load_dotenv(dotenv_path='../.env')

# Get the Ollama model from the environment variables
ollama_model = os.getenv("OLLAMA_MODEL")

# Initialize the Ollama LLM
llm = Ollama(model=ollama_model)

# Path to the document
doc_path = 'document.txt'

# Load the document
loader = TextLoader(doc_path)
docs = loader.load()

# Create the summarization chain
# The 'stuff' chain type is simple and works well for single documents.
chain = load_summarize_chain(llm, chain_type="stuff")

# Run the chain and get the summary
summary = chain.invoke(docs)

# Print the summary
print("--- Original Document ---")
with open(doc_path, 'r') as f:
    print(f.read())
print("\n--- Summary ---")
print(summary['output_text'])

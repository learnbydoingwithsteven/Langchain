import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain

# Load environment variables
load_dotenv(dotenv_path='../.env')
ollama_model = os.getenv("OLLAMA_MODEL")

# Initialize Ollama LLM and Embeddings
llm = Ollama(model=ollama_model)
embeddings = OllamaEmbeddings(model=ollama_model)

# 1. Load the document
loader = TextLoader('knowledge.txt')
docs = loader.load()

# 2. Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)

# 3. Create a FAISS vector store from the documents
vector = FAISS.from_documents(documents, embeddings)

# 4. Create a prompt template
prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

# 5. Create a stuff documents chain
document_chain = create_stuff_documents_chain(llm, prompt)

# 6. Create a retriever
retriever = vector.as_retriever()

# 7. Create the retrieval chain
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# 8. Run the chatbot
if __name__ == "__main__":
    print("RAG Q&A Chatbot is running! Ask questions about the knowledge base. Type 'exit' to quit.")
    while True:
        user_question = input("You: ")
        if user_question.lower() == 'exit':
            break
        response = retrieval_chain.invoke({"input": user_question})
        print(f"Bot: {response['answer']}")

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from memory_module import build_memory
import os

def build_vector_store(doc_path: str):
    print("📚 Loading and indexing documents...")

    loader = TextLoader(doc_path)
    raw_docs = loader.load()
    
    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=50)
    documents = splitter.split_documents(raw_docs)

    embedding_model = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(documents, embedding_model)

    print(f"✅ Indexed {len(documents)} document chunks.")
    return vector_store

def build_rag_agent(doc_path: str = "data/knowledge_base.txt"):
    llm = ChatOpenAI(temperature=0, model_name="gpt-4")
    vector_store = build_vector_store(doc_path)

    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    memory = build_memory()

    rag_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=True
    )

    print("✅ Agentic RAG chatbot is ready.")
    return rag_chain

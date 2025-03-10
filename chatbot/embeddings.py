from logger import logging
from exception import customexception
import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from chatbot.data_ingestion import load_data
from dotenv import load_dotenv
import os


def download_gemini_embedding(documents):
    try:
       load_dotenv()
       google_api_key=os.getenv("GOOGLE_API_KEY")
       logging.info(f"downloading gemini embedding...")
       text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
       docs = text_splitter.split_documents(documents)         
       embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=google_api_key)
       logging.info(f"embedding downloaded successfully")
       vector_store = FAISS.from_documents(docs, embeddings)
       vector_store.save_local("faiss_index")
       logging.info(f"Index created successfully")
       return embeddings
    except Exception as e:
        logging.info(f"execption in downloading embedding model")
        raise customexception(e,sys)
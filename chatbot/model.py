from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from logger import logging
import sys
from dotenv import load_dotenv
import os
from exception import customexception

def load_model():
    load_dotenv()
    google_api_key=os.getenv("GOOGLE_API_KEY")
    logging.info(f"Model is loading...")
    model=ChatGoogleGenerativeAI(model="models/gemini-1.5-pro",api_key=google_api_key)
    return model

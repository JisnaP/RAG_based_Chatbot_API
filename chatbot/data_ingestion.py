import sys
from logger import logging
from exception import customexception
from langchain_community.document_loaders import WebBaseLoader

def load_data():
    """
    Loads data from a website brainlox.com
    
    
    Returns: A list of specific loaded text documents
    
    """
    try:
      logging.info(f"Data loading started ...")
      loader = WebBaseLoader("https://brainlox.com/courses/category/technical")
      documents = loader.load()

      logging.info(f"logging completed")
      return documents
    except Exception as e:
      logging.info(f"exception in loading data")
      raise customexception(e,sys)
      
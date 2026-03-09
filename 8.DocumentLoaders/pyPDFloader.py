from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pathlib import Path

load_dotenv()

path =Path(__file__).parent /'demo.pdf'
loader = PyPDFLoader(path)
docs = loader.load()
# print((docs[0].page_content))
print((docs[1].metadata))
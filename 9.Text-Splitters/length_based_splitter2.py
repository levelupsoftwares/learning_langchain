from langchain_community.document_loaders import  PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from pathlib import Path

docpath = Path(__file__).parent.parent /"8.DocumentLoaders" / "demo.pdf"
doc = PyPDFLoader(docpath)

doc_text = doc.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    separator='',
    chunk_overlap=0,
)
result = splitter.split_documents(doc_text)
print(result[0].page_content)

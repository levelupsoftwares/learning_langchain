from langchain_community.document_loaders import DirectoryLoader ,TextLoader , PyPDFLoader
from pathlib import Path


loader = DirectoryLoader(
    path=Path(__file__).parent/ 'demoDir',
    glob=('*.pdf'),
    loader_cls=PyPDFLoader

)
doc = loader.load()
print(doc[0].page_content)
print(doc[7].metadata)
print(len(doc))
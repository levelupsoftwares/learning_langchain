from langchain_community.document_loaders import DirectoryLoader ,TextLoader , PyPDFLoader
from pathlib import Path


loader = DirectoryLoader(
    path=Path(__file__).parent/ 'demoDir',
    glob=('*.pdf'),
    loader_cls=PyPDFLoader

)
doc = loader.lazy_load()
for page in doc:
    print(page.page_content)

from pathlib import Path
from langchain_community.document_loaders import TextLoader

file = Path(__file__).parent / "demoText.txt"

# file = os.listdir('demoText')
loader = TextLoader(file)
docs = loader.load()
# print(type(docs))
print(type(docs[0]))
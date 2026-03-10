from langchain_community.document_loaders import CSVLoader
from pathlib import Path

csvFile = Path(__file__).parent/'demo.csv'

loader = CSVLoader(csvFile)
fileContent = loader.load()
print(fileContent[0].page_content)
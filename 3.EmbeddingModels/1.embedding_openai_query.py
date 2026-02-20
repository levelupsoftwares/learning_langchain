from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "it is the first line of para",
    "second line of para",
    "third line of para"
]

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
embedding.embed_query('this is setence ')

embedding.embed_documents(documents) # when we want to embed documents we use this keywords 

print(str(embedding))
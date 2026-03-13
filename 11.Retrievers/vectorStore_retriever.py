from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name='my-collection'
)

retriever= vector_store.as_retriever(search_kwargs={'k':1})

query = 'what is chroma used for'

result = retriever.invoke(query)
print(result)

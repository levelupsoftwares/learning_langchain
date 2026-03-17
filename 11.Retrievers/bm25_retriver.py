from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever # used for word matches
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


documents = [
    Document(page_content="""Solar panels convert sunlight into electricity using photovoltaic cells. Their efficiency depends on sunlight intensity, panel angle, and temperature. In many countries, rooftop solar systems help reduce electricity bills and lower dependence on fossil fuels."""),
    Document(page_content="""
    Machine learning allows computers to improve performance by learning from data instead of following fixed rules. A recommendation system, for example, studies user behavior to predict which movie or product someone may prefer next."""),
    Document(page_content="""
    Drip irrigation delivers water directly to plant roots through narrow tubes. This method reduces evaporation, saves water, and improves crop productivity, especially in dry regions where water resources are limited."""),
    Document(page_content="""
    A black hole forms when a very massive star collapses under its own gravity. Its gravitational pull becomes so strong that even light cannot escape, which makes direct observation extremely difficult."""),
    Document(page_content="""
    Two-factor authentication adds an extra security layer by requiring both a password and a second verification step, such as a mobile code. This greatly reduces the risk of unauthorized account access.""")
]

embedding_model = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)
# vector_store = Chroma.from_documents(
    # documents=documents,
    # embedding=embedding_model,
    # collection_name='testing'
# )
retriever  = BM25Retriever.from_documents(documents=documents)

print(retriever.invoke('How do rooftop systems lower electricity costs?')[0].page_content)
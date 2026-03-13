from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results=1,
    lang='en'
)

query= 'pakistan and iran relations in perspective of USA'

docs = retriever.invoke(query)

print(docs)
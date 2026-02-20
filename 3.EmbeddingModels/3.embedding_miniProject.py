#              similarity between Doc and user query
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import  cosine_similarity
# from numpy import np
document =[
    'ALi is very famous Eng and he secure the top tier firm as swe',
    'Usman is very famous Ai Eng and he secure the top tier firm as AI swe',
    'Junaid is very famous Web-Dev and he secure the top web firm',
    'Qasim was very famous Eng and he secure the top tier firm as sre',
]
query= 'web dev'
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
doc_vector = embedding.embed_documents(document)
query_vector = embedding.embed_query(query)

scores = cosine_similarity([query_vector],doc_vector)[0]
index ,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print("user query: ",query)
print(document[index])
print("simlarity score",score)
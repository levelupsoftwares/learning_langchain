from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

document=[
    'laptop have many components: like mousepad, screen, cpu and gpu',
    'pricing of laptop may differ according to their specs and model',
    'the higher the laptop have configuration the higher the price goes',
    'with lowest laptop configuration range from 30k to so on..'
]
user_query ="cheapeat laptop start from"

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

vector_of_document = embedding.embed_documents(document)
vector_of_query = embedding.embed_query(user_query)


result= cosine_similarity([vector_of_query],vector_of_document)[0]
key,indexs = (sorted(list(enumerate(result)),key=lambda x:x[1])[-1])
print("user Query",user_query)
print("the best similtrt findin in this line: " , document[key])




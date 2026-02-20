from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = 'im learning ai engineering from campusx'
document = ['this is the first para of the Doc',
            'second para of the Doc',
            'third para of the Doc']


vector_of_query =  embedding.embed_query(text) #for query
# print(str(vector_of_query))
vector_of_Doc = embedding.embed_documents(document)
print(str(vector_of_Doc))
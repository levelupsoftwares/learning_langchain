from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
ytt_api = YouTubeTranscriptApi()
api_output =ytt_api.fetch('JkJOZewGTU4') # fetching transcript via yt video id

video_transcript =''

for transcript in api_output:
    video_transcript += transcript.text +" "

# print(video_transcript)
# splitting transcript into chunks 
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50
)
splitted_transcript = splitter.split_text(video_transcript)


embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
llm_model=ChatGroq(model='openai/gpt-oss-120b')
parser = StrOutputParser()
prompt_template = PromptTemplate(
    template='You are helpfull assistant. This is the youtube video im watching what its means :{query} answer only by with given context: \n{context} and answer should be small',    
    input_variables=['query','context']
)

# # # vector store
vector_store = Chroma.from_texts(
    texts=splitted_transcript,
    embedding=embedding_model
)

# #retrievers
dense_retriever = vector_store.as_retriever(
    search_type='similarity',
    search_kwargs={'k':4}
)
base_retriever = BM25Retriever.from_texts(
    texts=splitted_transcript,
    search_kwargs={'k':4}
)

 #hybrid retriever
hybrid_retriever = EnsembleRetriever(
    retrievers=[dense_retriever,base_retriever],
    weights=[0.5,0.5]
)

def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)

chain = (
    {
        "context":hybrid_retriever | format_docs,
        'query':RunnablePassthrough()
    }
    | prompt_template
    | llm_model
    | parser
)

# chain =  hybrid_retriever|prompt_template | llm_model | parser

print(chain.invoke('gen ai engineer'))
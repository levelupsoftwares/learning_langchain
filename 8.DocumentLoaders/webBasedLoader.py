from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model='openai/gpt-oss-120b'
)
parser = StrOutputParser()

prompt = PromptTemplate(
    template='asnwer this {query} from {data_source}',
    input_variables=['query','data_source']
)


url = 'https://en.wikipedia.org/wiki/Chroma_(vector_database)'
loader = WebBaseLoader(url)

docs = loader.load()
# print(docs[0].metadata)


chain = prompt | model | parser

print(chain.invoke({'query':'chroma initial relase date','data_source':docs[0].page_content}))
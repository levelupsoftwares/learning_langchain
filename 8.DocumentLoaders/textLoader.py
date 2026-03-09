from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
model = ChatGroq(model='openai/gpt-oss-120b')
parser = StrOutputParser()

file  = Path(__file__).parent /'demoText.txt'

loader = TextLoader(file)
data = loader.load()
prompt = PromptTemplate(
    template='summarize in 2 line given {docs}',
    input_variables=['docs']
)
result = prompt | model | parser
print(result.invoke({'docs':data[0].page_content}))
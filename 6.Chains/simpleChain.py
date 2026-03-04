from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)

parser = StrOutputParser()

model =ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template='explain the {topic} in 5 pointers ',
    input_variables=['topic'],
)

chain =  template | model | parser
result  = chain.invoke({'topic':'book',})
# print(result)
# chain.get_graph().print_ascii() #when want visual representation of chain pipline

from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
parser = StrOutputParser()

llm =HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='make an exaplanation on {topic}',
    input_variables=['topic'],
)
template2 = PromptTemplate(
    template='Summarize this {response} in 5 pointers',
    input_variables=['response']
)


chain = template1 | model |parser | template2 | model |parser
result = chain.invoke({'topic':'laptop'})
print(result)
# chain.get_graph().print_ascii()
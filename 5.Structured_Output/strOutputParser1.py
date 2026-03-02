from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task ='text-generation'
)
model = ChatHuggingFace(llm = llm)

template1 = PromptTemplate(
    template='Explain this {topic} in funny way',
    input_varibales  = ['topic'] 
)
template2 = PromptTemplate(
    template='summarize this {llmResponse} in 4 lines',
    input_varibales = ['llmResponse']
)

parser = StrOutputParser() 
chain  = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'laptop'})
print(result)
# prompt1 = template1.invoke({'topic':'laptop'})
# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'llmResponse':result.content})
# result1 = model.invoke(prompt2)
# print(result1.content)
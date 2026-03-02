from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm  = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation',
    # pipeline_kwargs=dict(
    #     temperature=0.3,
    #     max_new_tokens=100
    # )
)

model = ChatHuggingFace(llm=llm)

template1= PromptTemplate(
    template =' Write a detailed report on {topic}',
    input_varibales = ['topic']
)



template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text: {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({
    'topic':'black hole'
})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)
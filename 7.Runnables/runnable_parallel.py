from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model='openai/gpt-oss-120b'
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='write an very short post for x on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='write an post for linkedin on {topic}',
    input_variables=['topic']
)

runnable_parallel=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})

result = runnable_parallel.invoke({'topic':'Gen AI'})

# print(type(result)) Dict
print(result)
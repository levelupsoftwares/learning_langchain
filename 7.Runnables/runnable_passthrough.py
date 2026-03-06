from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel ,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
parser = StrOutputParser() 

model = ChatGroq(
    model='openai/gpt-oss-120b'
)
prompt1=PromptTemplate(
    template='write a joke on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a 2 line explanation on {joke}',
    input_variables=['topic']
)

joke_creation = RunnableSequence(prompt1,model,parser)

parallel_runnable = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

result = RunnableSequence(joke_creation,parallel_runnable)
final= result.invoke({'topic':'pen'})
print(final)
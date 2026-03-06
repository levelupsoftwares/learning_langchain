from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model='openai/gpt-oss-120b'
)

parser = StrOutputParser()

prompt1= PromptTemplate(
    template='give me joke on {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='exaplin this joke {response} in 2 lines',
    input_variables=['topic']
)

runnable_sequence = RunnableSequence(prompt1 ,model ,parser,prompt2,model,parser)
result= runnable_sequence.invoke({'topic':'computer'})
print(result)
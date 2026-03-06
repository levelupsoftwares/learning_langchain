from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda ,RunnableSequence ,RunnablePassthrough,RunnableParallel,RunnableBranch
from dotenv import load_dotenv

load_dotenv()


model = ChatGroq(
    model='openai/gpt-oss-120b'
)
parser = StrOutputParser()

prompt1=PromptTemplate(
    template='Write a report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Summarize the following {text} in 100 words',
    input_variables=['text']
)

report_generate_chain = RunnableSequence(prompt1 , model ,parser)

runnable_branch = RunnableBranch(
    (lambda x:len(x.split()) > 400,prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generate_chain ,runnable_branch)
print(final_chain.invoke({'topic':'car'}))
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda ,RunnableSequence ,RunnablePassthrough,RunnableParallel
from dotenv import load_dotenv

load_dotenv()
def wordCount(text):
    return len(text.split())

model = ChatGroq(
    model='openai/gpt-oss-120b'
)
parser = StrOutputParser()

prompt=PromptTemplate(
    template='Make an joke on {topic}',
    input_variables=['topic']
)

joke_runnable = RunnableSequence(prompt,model,parser)

paral_runnable = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word':RunnableLambda(wordCount)
})

final_runnnable = RunnableSequence(joke_runnable,paral_runnable)


result= final_runnnable.invoke({'topic':'ice'})
print(result)
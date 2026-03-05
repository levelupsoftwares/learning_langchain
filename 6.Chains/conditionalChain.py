from langchain_groq import ChatGroq
# from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser ,PydanticOutputParser
from langchain_core.runnables import RunnableParallel ,RunnableBranch ,RunnableLambda
from pydantic import BaseModel ,Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

class Feedback_format(BaseModel):
    sentiment:Literal['positive','negative'] = Field(description='give the sentiment of the feedback')

model = ChatGroq(model='openai/gpt-oss-120b')
parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object = Feedback_format)

prompt1 = PromptTemplate(
    template='Analyze the sentiment of the following feedback text into positive or negative \n{feedback} \n{feedback_format}',
    input_variables=['feedback'],
    partial_variables={'feedback_format':parser2.get_format_instructions()}
)

prompt2=PromptTemplate(
    template='write a appropriate response for possitive feedback \n{feedback}',
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template='write a appropriate response for negative feedback \n{feedback}',
    input_variables=['feedback']
)


classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive',prompt2 | model |parser),
    (lambda x:x.sentiment == 'negative',prompt3 | model |parser),
    RunnableLambda(lambda x:"Not find the sentiment") 
)
chain = classifier_chain | branch_chain
result = chain.invoke({'feedback':'very helpless device'})
# print(result)
chain.get_graph().print_ascii()
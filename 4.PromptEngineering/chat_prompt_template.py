# for list of dynnamic multiturn conversation we use ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

chat_template = ChatPromptTemplate([
    ('system','You are {Domain} specialist'),
    ('human','Exalain in plain words, what is {topic}')
    # SystemMessage(content='You are {Domain} specialist'), # It's not working so we use upper 
    # HumanMessage(content='Exalain in plain words, what is {topic}')
])
prompt= chat_template.invoke({'Domain':'Cricket','topic':'lbw'})
print(prompt)
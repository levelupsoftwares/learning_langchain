# MessagesPlaceholder(help to retrive )and store the chat history ) make llm more context aware of past chats and 
# give a better response of current query
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

chat_template =ChatPromptTemplate([
    ('system','You are Help Full assitance with friendly tone '),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
]) 
chat_history= []

with open('4.PromptEngineering/chat_history.txt') as file:
    chat_history.extend(file.readlines())

# print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history,
                      'query':'where is my refund'
                      })
print(prompt)
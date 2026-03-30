from langchain_core.tools import tool
from langchain_core.messages import HumanMessage , ToolMessage , SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import requests

load_dotenv()

llm = ChatGroq(model='llama-3.3-70b-versatile')

message = []
query = HumanMessage('im visiting Pakistan and i want to convert 10 usd into pkr ,how much pkr i get in exchange') 
System_Message = SystemMessage('You are a very helpfull crrency exchanger assistan, When a tool provides a conversion result,always use that exact result in your answer. Never use your own knowledge for rates.')
message.extend([query,System_Message])

url = os.getenv("EXCHANGE_RATE_KEY")

#tool
@tool
def currency_converter(currency_have,currency_want,value):
    """Currency Converter Tool:take three parameters currency_have ,currency_want and value and return result"""
    currency_have = currency_have.upper()
    currency_want = currency_want.upper()

    api_for_call = f'{url}/pair/{currency_have}/{currency_want}'
    response  = requests.get(api_for_call)
    data = response.json()
    return data['conversion_rate'] *value


# currency_converter('usd','pkr')
# print(currency_converter('pkr','usd',279))

#Bind Tool
llm_with_tool = llm.bind_tools([currency_converter])

tool_suggestion = llm_with_tool.invoke(message)
message.append(tool_suggestion)

#tool execution

tool_call = tool_suggestion.tool_calls[0]
tool_execute = currency_converter.invoke(tool_call)

message.append(tool_execute)

#llm answer using tool output

llm_final_answer=llm.invoke(message)
print(llm_final_answer.content)

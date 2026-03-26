from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-120b')

@tool 
def add(a:int,b:int)->float:
    """add two numbers"""
    return a+b

llm_with_tools = llm.bind_tools([add]) #tool binding
result  = llm_with_tools.invoke('add 1 with 8') #llm suggest which tools to call

# print(result.tool_calls)
# Tool execution
# print(add.invoke({'name': 'add', 'args': {'a': 1, 'b': 8}, 'id': 'fc_2f0b9558-20d8-457d-9862-e68352fc3dff', 'type': 'tool_call'}))  
print(add.invoke(result.tool_calls[0]['id']))  
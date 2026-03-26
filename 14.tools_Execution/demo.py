from langchain_core.tools import tool 
from langchain_groq import ChatGroq
from dotenv import  load_dotenv

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-120b')

@tool
def mul(a,b):
    """Multiply Two integer and return result in float"""
    return a*b

#tool binding
binded_llm = llm.bind_tools([mul])

# llm suggest tool call 
suggested_tool = binded_llm.invoke('can u multiply 2 with 4').tool_calls
print(f"suggested Tool: {suggested_tool[0]['args']}")


#tool invoke
print(mul.invoke(suggested_tool[0]['args']))
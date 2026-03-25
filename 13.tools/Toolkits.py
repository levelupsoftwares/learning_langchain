# collection of tools that work to-gather to deliver same purpose 

from langchain_core.tools import tool
# from langchain_core.tools import tOOL

#custom tools
@tool
def add(a,b):
    """"Add two numbers"""
    return a+b


@tool
def multiply(a,b):
    """"Multiply two numbers"""
    return a*b

class MathToolkit:
    def get_tools(self):
        return [add, multiply]
    
toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.invoke({'a':7,'b':2}))
from langchain_core.tools import tool

@tool                                # tool decorater help to create a custom tool
def addition(a:int,b:int)->float:
    """"Addining two numbers"""      # description in docstring help to llm understand the role or functionality of the tool
    return a + b

result = addition.invoke({'a':1,'b':7})

print(result)
print(addition.name) 
print(addition.description)
print(addition.args)
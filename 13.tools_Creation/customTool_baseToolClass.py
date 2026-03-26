from langchain_core.tools import BaseTool
from pydantic import BaseModel,Field
from typing import Type

class formating(BaseModel):
    a: int = Field(description='first number to multiply')
    b: int = Field(description='second number to multiply')

class tools(BaseTool):
    name:str = 'multiply'
    description:str = 'Multiply two numbers'
    args_schema:Type[BaseModel] =formating

    def _run(self,a:int , b:int) ->int:
        return a *b
    
custom_tool=tools()
print(custom_tool.invoke({'a':5,'b':2}))
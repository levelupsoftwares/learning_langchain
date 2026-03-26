from langchain_core.tools import StructuredTool
from pydantic import BaseModel , Field


class MultipleInput(BaseModel):
    a: int = Field(required=True,description='the first number to add')
    b: int = Field(required=True,description='the second number to add')

def multiply_fun(a,b):
    return a * b

tool = StructuredTool.from_function(
    func=multiply_fun,
    name='multiply',
    description='muktiplying two numbers',
    args_schema=MultipleInput
)

resutl = tool.invoke({'a':3,'b':9})
print(resutl)
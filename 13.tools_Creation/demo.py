from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class format(BaseModel):
    a:int = Field(description='First num to subtract')
    b:int = Field(description='Second num to subtract')

def subtractor(a,b)->float:
    return a-b

tool = StructuredTool.from_function(
    func=subtractor,
    name='subt',
    description='Subtracting two numbers',
    args_schema=format
)
print(tool.invoke({'a':9,'b':6}))
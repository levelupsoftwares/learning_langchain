from langchain_core.tools import tool
from langchain_core.messages import HumanMessage ,AIMessage,ToolMessage
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model='openai/gpt-oss-120b')
 
query = HumanMessage('multiply 8 with 9')

message = [query]

# print(message)

@tool
def mult(a:int,b:int)->float:
    """Multiply Two integers and return result in Float"""
    return a*b

#bind tool
llm_with_tool = llm.bind_tools([mult])

#llm sugesst tool
tool_sugestion = llm_with_tool.invoke(message)
# print((tool_sugestion))

message.append(tool_sugestion)
# print(message)


#Tool execution
tool_call = tool_sugestion.tool_calls[0]
tool_result = mult.invoke(tool_call)

#wrap tool result
tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call['id']
)
message.append(tool_message)

#final llm answer
final_response = llm_with_tool.invoke(message)
print(final_response.content)




from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,ToolMessage,SystemMessage

load_dotenv()

llm=ChatGroq(model='llama-3.3-70b-versatile')

@tool
def currency_converter(have:str,want:str,value:float)->float:
    """
        Always use this tool when user asks currency conversion.
            Args:
                have: source currency
                want: target currency
                value: amount
    """
    have = have.lower()
    want = want.lower()

    if want in ['pkr' ,'usd' ,'aud']:
        if have == 'pkr':
            if want == 'usd':
                return value/279
            elif want == 'aud':
                return value /193
        elif have == 'usd':
            if want == 'aud':
                return value + 0.45
            elif want  == 'pkr':
                return value * 279
        elif have == 'aud':
            if want == 'usd':
                return value-0.45
            elif want == 'pkr':
                return value *193
    else:
        return 'Currency not supported Yet'
    
query = HumanMessage('convert 1usd to pkr')
system_message = SystemMessage(
    content='You are a currency assistant. When a tool provides a conversion result,always use that exact result in your answer. Never use your own knowledge for rates.'
)
message = []
message.append(query)
message.append(system_message)

llm_with_tool = llm.bind_tools([currency_converter],tool_choice="currency_converter")

ai_suggestion = llm_with_tool.invoke(message) #AIMessage


message.append(ai_suggestion)

#tool execution
tool_call = ai_suggestion.tool_calls[0]
tool_result = currency_converter.invoke(tool_call)


tool_meesage = ToolMessage(
    content=str(tool_result),
    tool_call_id = tool_call['id']
)
message.append(tool_meesage)


llm_response = llm.invoke(message)
print(llm_response.content)
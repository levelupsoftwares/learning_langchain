from langchain_core.tools import tool 
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain_classic.agents import create_react_agent,AgentExecutor
from langchain_classic import hub

load_dotenv()
llm = ChatGroq(model = 'llama-3.3-70b-versatile')



search_tool = DuckDuckGoSearchRun()
@tool
def webSearch(query): 
    """"tool to Search on the web,take one parameter as query"""
    return search_tool.invoke(query)


# bind tool
llm_with_tool = llm.bind_tools([webSearch])

prompt = hub.pull('hwchase17/react')


#create the reAct agent with pulled prompt

agent = create_react_agent(
    llm=llm,
    tools=[webSearch],
    prompt=prompt
)

#   wrap it in agent-executer
agent_executer = AgentExecutor(
    agent=agent,
    tools=[webSearch],
    verbose=True
)

# invoke
response = agent_executer.invoke({"input":"what is capital of Pakistan and where i situatuted "})
print(response)
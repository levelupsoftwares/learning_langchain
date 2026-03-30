from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from langchain_classic import hub

from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model='openai/gpt-oss-120b')
browse = DuckDuckGoSearchRun()


@tool
def web_search(query):
    """web search tool:use tool for searching on the brwoser,give only one prarameter as input"""
    return browse.invoke(query)

agent = create_agent(model= llm,tools=[web_search],system_prompt="")
print(agent.invoke({"messages":[
    {"role":"user","content":"what is the capital of Pakistan"}
]}))
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from langchain_classic import hub

from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model='openai/gpt-oss-120b')
browse = DuckDuckGoSearchRun()
prompt = hub.pull("hwchase17/react")

@tool
def web_search(query):
    """web search tool:use tool for searching on the brwoser,give only one prarameter as input"""
    return browse.invoke(query)

agent = create_agent(model= llm,tools=[web_search],system_prompt="""You are a reasoning assistant.
                                                        Think carefully before using tools.
                                                        Use tools when external knowledge is needed.
                                                        Answer clearly after observation.""")
print(agent.invoke({"messages":[
    {"role":"user","content":"what is the capital of Pakistan"}
]}))



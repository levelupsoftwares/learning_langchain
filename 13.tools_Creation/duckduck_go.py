from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()
resutl = search_tool.invoke('who is the president of usa')
print(resutl)
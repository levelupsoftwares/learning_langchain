from langchain_ollama import ChatOllama


llm  = ChatOllama(
    model = 'coldAgent:latest'
)
result = llm.invoke('who are you?')
print(result)
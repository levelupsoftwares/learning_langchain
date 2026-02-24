from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="conversational"
)
model = ChatHuggingFace(llm=llm)

messesges = [
    SystemMessage('You are helpfull assisstance'),
    HumanMessage('diff btw langchian and langGrahp in only 2 lines')
] 
result = model.invoke(messesges)
messesges.append(AIMessage(content=result.content))
print(messesges)
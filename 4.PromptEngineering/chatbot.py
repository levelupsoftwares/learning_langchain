from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage ,SystemMessage,AIMessage

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
 repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
 task="conversational"
)
model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage('You have very friendly tone and not give response more then 2 lines')
]

while True:
    user_input=input("")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content= result.content))
    print(result.content)
print(chat_history)
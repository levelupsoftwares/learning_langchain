from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
 repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
 task="conversational"
)
model = ChatHuggingFace(llm=llm)

chat_history = []

while True:
    user_input=input("")
    chat_history.append('User: ' + user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append('AI: '+ result.content)
    print(result.content)
print(chat_history)
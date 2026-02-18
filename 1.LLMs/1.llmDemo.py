from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct',temperature=0,max_tokens=5) # temprature = creativity , max_tokens = output token restriction 
result = llm.invoke("how is elon musk")
print(result)

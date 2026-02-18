from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B",
    task ="text-generation",
    max_new_tokens=100
    # provider="hf-inference"
) 

model = ChatHuggingFace(llm=llm)
result = llm.invoke("what is the capital of USA")

print(result)
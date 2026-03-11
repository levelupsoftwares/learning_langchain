from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

text = """
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
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=150,
    chunk_overlap=0,
)

print(splitter.split_text(text))
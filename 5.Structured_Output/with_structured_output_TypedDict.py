from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from typing import TypedDict ,Annotated

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
    task='conversational'
)
model = ChatHuggingFace(llm=llm)

# schema
class dataFormat(TypedDict):
    summary:Annotated[str , 'A Breif summary of the review']
    sentiment:Annotated[str , 'possitive or negative']
    price:int

structured_model = model.with_structured_output(dataFormat)

result = structured_model.invoke("""
The MacBook Pro with the **M1 Max** chip delivers exceptional performance for demanding creative and professional workflows, combining strong CPU/GPU power with excellent battery life and a vibrant display.Price start from 1500 usd

**Pros:**
• Extremely capable for video editing, 3D work, and multitasking.
• Long battery life with efficient Apple Silicon design.

**Cons:**
• Expensive compared to other laptops.
• Newer Mac models (M3/M4/M5 chips) are faster and more efficient.
""")
print(result.content)


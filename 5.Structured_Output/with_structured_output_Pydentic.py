from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel , Field
from typing import Literal , Optional

load_dotenv()


llm=ChatGroq(
    model='openai/gpt-oss-120b',
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)



class review(BaseModel):
    key_theme:list[str] = Field(description='A brief summary of the review')
    sentiments: Literal['positive','negative','neutral'] = Field(description='Return sentiments of the review either positive ,negative or neutral')
    pros: Optional[list[str]] = Field(default=None, description='Write down all the pros inside a list')
    cons: Optional[list[str]] =Field(default=None , description='Write down all the cons inside a list')
    name:Optional[str] = Field(default=None,description='Write the name of the reviewer')



structured_output = llm.with_structured_output(review)
# print(structured_output)
person_review ='The M1 is a massive leap in performance and efficiency. Great for students, developers, and content creators. Power users with extreme GPU needs might feel limited. Small chip, big impact. blazing fast for daily tasks and creative work, excellent battery life, silent performance, smooth macOS experience, good value compared to older Intel Macs.RAM and SSD not upgradeable, not ideal for heavy 3D or high-end gaming, some legacy software may not work perfectly, limited external monitor support'
result = structured_output.invoke(person_review)
print(result)
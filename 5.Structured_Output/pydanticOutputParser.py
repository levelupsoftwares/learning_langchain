from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from dotenv import load_dotenv

load_dotenv()
class knowledge(BaseModel):
    topic_name:str= Field(description='Name of the topic')
    topic_catogrey:str=Field(description='Catogrey of the topic')


llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)
model = ChatHuggingFace(llm = llm)
parser = PydanticOutputParser(pydantic_object=knowledge)

template = PromptTemplate(
    template='Explain me this {topic} \n {format}',
    input_variables=['topic'],
    partial_variables={'format':parser.get_format_instructions()}
)
prompt=template.invoke({'topic':'book'})
result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)
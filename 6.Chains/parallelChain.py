from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()


llm=HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)

model1 = ChatHuggingFace(llm=llm)

model2 = ChatGroq(
    model='openai/gpt-oss-120b',
)

parser = StrOutputParser()

template1 = PromptTemplate(
    template='Generate a notes from the {text}',
    input_variables=['text']
)

template2 = PromptTemplate(
    template='Generate a quiz from the given {text}',
    input_variables=['text']
)
template3 = PromptTemplate(
    template='merge the give notes and quiz into single document \notes:{notes},  quiz:{quiz}',
    input_variables=['notes','quiz']
)


parallel_chain = RunnableParallel({
    'notes' : template1 | model1 | parser,
    'quiz' : template2 | model2 | parser 
})

merge_chain = template3 | model2 | parser

chain= parallel_chain | merge_chain

text= """Quantum computing is an emergent field of computer science and engineering that harnesses the unique qualities of quantum mechanics to solve problems beyond the ability of even the most powerful classical computers.

The field of quantum computing includes a range of disciplines, including quantum hardware and quantum algorithms. While still in development, quantum technology will soon be able to solve complex problems that classical supercomputers can’t solve (or can’t solve fast enough).

By taking advantage of quantum physics, large-scale quantum computers would be able to tackle certain complex problems many times faster than modern classical machines. Quantum computers have the potential to solve certain problems in minutes or hours that would otherwise take conventional machines millennia to complete.

Quantum mechanics, the study of physics at small scales, reveals surprising fundamental natural principles. Quantum computers specifically harness these phenomena to access mathematical methods of solving problems not available with classical computing alone."""

result = chain.invoke({'text':text})
print(result)
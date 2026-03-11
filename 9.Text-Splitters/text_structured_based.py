from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """LangChain is an open source framework with a prebuilt agent architecture and integrations for 
any model or tool—so you can build agents that adapt as fast as the ecosystem evolves

LangChain is the easy way to start building completely custom agents and applications powered by 
LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and more. 
LangChain provides a prebuilt agent architecture and model integrations to help you get started
quickly and seamlessly incorporate LLMs into your agents and applications.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    separators='',
    chunk_overlap=0
)
result= splitter.split_text(text)
print(len(result))
print((result))
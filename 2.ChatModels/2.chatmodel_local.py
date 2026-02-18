from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.3,
        max_new_tokens=10
    )
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("who is bill gates")
print(result.content)
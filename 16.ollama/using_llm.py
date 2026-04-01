import ollama

response = ollama.generate(model='llama3.2:1b',prompt='rose flower scientific name')
print(response)
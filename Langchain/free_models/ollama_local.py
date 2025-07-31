from langchain_community.llms import Ollama

llm = Ollama(model="llama2", base_url="http://localhost:11434")

res = llm.invoke("Who are you? What do you do?")

print(res)
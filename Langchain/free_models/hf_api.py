from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("Can I learn Photoshop within the free trial period?")

try:
    res = model.invoke("Can I learn Photoshop within the free trial period?")
    print(res)
    print(res.content)
except Exception as e:
    print(f"Error: {e}")
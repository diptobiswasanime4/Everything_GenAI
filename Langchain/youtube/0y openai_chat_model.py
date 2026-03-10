from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-3.5-turbo")

res = model.invoke("What are the top 3 Game Engines, top 3 Frameworks, top 3 Languages for Indie GameDevs?")

print(res)
print(res.content)
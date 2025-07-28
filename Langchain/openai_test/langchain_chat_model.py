from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-3.5-turbo')

res = model.invoke("Top 5 Game Engines and top 5 Frameworks for Indie GameDevs?")

print(res)
print(res.content)
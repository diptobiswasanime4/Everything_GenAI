from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = "gpt-3.5-turbo-instruct")

res = llm.invoke("What are the top 3 Game Engines, Frameworks, Languages for Indie GameDevs?")

print(res)
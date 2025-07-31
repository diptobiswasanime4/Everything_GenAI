from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

res = model.invoke("What are the most popular Adobe Apps?")

print(res)
print(res.content)
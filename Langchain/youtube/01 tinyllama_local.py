from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# res = model.invoke("Can I learn Photoshop within the free trial period?")

# print(res)
# print(res.content)

res_chunk = model.stream("Can i learn PS in 7 days?")

for chunk in res_chunk:
    print(chunk.content, end="", flush=True)

# while True:
#     user_input = input("Arya: ")
#     if user_input == "exit":
#         break

#     print("AI: ", end="", flush=True)

#     for chunk in model.stream(user_input):
#         print(chunk.content, end="", flush=True)

#     print()
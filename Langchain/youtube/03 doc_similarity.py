from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs = [
    "The Russia-Ukraine war continues to influence global energy markets and security alliances.",
    "The United States and China are competing for technological and economic dominance.",
    "India is strengthening its strategic partnerships through the QUAD alliance.",
    "The European Union is working to reduce dependency on Russian natural gas.",
    "Tensions in the South China Sea involve China, Vietnam, the Philippines, and other regional powers.",
    "NATO has expanded its strategic focus after the Ukraine conflict.",
    "China's Belt and Road Initiative aims to expand infrastructure and trade links across Asia, Africa, and Europe.",
    "The Middle East geopolitical landscape is shifting with new diplomatic agreements.",
    "Iran's nuclear program remains a major topic in global diplomatic negotiations.",
    "Israel and several Arab countries have improved relations through recent normalization agreements.",
    "The Arctic region is gaining geopolitical importance due to melting ice and new shipping routes.",
    "Cybersecurity and cyber warfare are becoming central concerns in international relations.",
    "Africa is becoming a key region for global competition over natural resources and investment.",
    "Taiwan remains a sensitive geopolitical flashpoint between China and the United States.",
    "Global supply chains are being reshaped due to geopolitical tensions and economic security concerns."
]

query = "Tell me about Cybersecurity."

doc_embeddings = embedding.embed_documents(docs)
query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings)

print(scores)
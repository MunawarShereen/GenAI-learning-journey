from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load free Hugging Face embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

document = [
    "Pakistan cricket is known for its unpredictability and raw talent.",
    "The team won the ICC Cricket World Cup in 1992 under Imran Khan.",
    "It has produced legendary players like Wasim Akram and Waqar Younis.",
    "Pakistan is famous for its fast bowlers and passionate fans.",
    "The rivalry with India is one of the most watched sporting events."
]

query = "tell me about Imran Khan"

# Create embeddings
vectors = model.encode(document)
query_vector = model.encode([query])[0]

# Compute cosine similarity
scores = cosine_similarity([query_vector], vectors)[0]

# Find best matching document
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print("Query:", query)
print("Best Match:", document[index])
print("Similarity Score:", score)

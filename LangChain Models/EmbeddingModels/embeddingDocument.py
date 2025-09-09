from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

dcoument = [
    "Islamabad is the capital of Pakistan",
    "Karachi is the largest city of Pakistan",
    "Lahore is the cultural hub of Pakistan",
    "Peshawar is the capital of Khyber Pakhtunkhwa",
    "Quetta is the capital of Balochistan",
    "You can write whatever you want"
]

vector = embeddings.embed_documents(dcoument)
print(str(vector))

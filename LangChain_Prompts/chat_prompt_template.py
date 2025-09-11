from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
model = "meta-llama/Llama-3.3-70B-Instruct:cerebras"
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)

def create_system_message(domain):
    return f"you are a {domain} expert"

def create_user_message(topic):
    return f"explain in the easy and simple way about {topic}"

# Create messages
messages = [
    {"role": "system", "content": create_system_message("AI")},
    {"role": "user", "content": create_user_message("LLM")}
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100
)

result = response.choices[0].message.content
print("Response:", result)
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
model="meta-llama/Llama-3.3-70B-Instruct:cerebras"
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)

chat_history = [{
    "role": "system",
    "content": "You are a helpful research assistant. Provide concise and accurate answers based on the user's questions."
}
]

while True:
    user_input = input("Enter your question (or type 'exit' to quit): ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == 'exit':
        break
    
    response = client.chat.completions.create(
        model=model,
        messages=chat_history,
        max_tokens=60
    )
    
    result = response.choices[0].message.content
    chat_history.append({
        "role": "assistant",
        "content": result
    })
    print("AI:", result)
    
for message in chat_history:
    print(f"{message['role']}: {message['content']}")
    
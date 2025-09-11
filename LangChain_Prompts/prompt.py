import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load Hugging Face token from .env
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    st.error("❌ HF_TOKEN not found. Please set it in your .env file.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

# Streamlit UI
st.title("Research Tool")
user_input = st.text_input("Enter your question:")

if st.button("Generate Answer"):
    if user_input:
        with st.spinner("Generating..."):
            try:
                # Call the API directly here
                response = client.chat.completions.create(
                    model="meta-llama/Llama-3.3-70B-Instruct:cerebras",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful research assistant. Provide concise and accurate answers based on the user's questions.",
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                )
                # Extract the response content
                result = response.choices[0].message.content
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question first.")
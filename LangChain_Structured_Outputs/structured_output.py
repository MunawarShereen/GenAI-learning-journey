from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import TypedDict,Annotated,List,Optional

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
model="meta-llama/Llama-3.3-70B-Instruct:cerebras"
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, 'The overall sentiment of the review, either "Positive", "Negative", or "Neutral"']
    key_themes: Annotated[List[str], "A list of key themes mentioned in the review"]
    pros: Annotated[Optional[List[str]], "A list of positive aspects mentioned in the review"]
    cons: Annotated[Optional[List[str]], "A list of negative aspects mentioned in the review"]
  
  
user_reiview = """I recently purchased the new XYZ smartphone, and overall, 
I am quite satisfied. The design is sleek and premium, 
and the display is vibrant with excellent color accuracy. The battery life is
impressive, lasting me a full day with heavy usage. However, the camera sometimes
struggles in low-light conditions, and the phone feels slightly heavy when held for
long periods. The software is smooth, but I noticed occasional lags when switching 
between apps. Overall, a solid phone for its price, but not perfect.""" 
    
prompt = f"""
Analyze the following review and respond with JSON only.
Review = "{user_reiview}"

Format:
{{
  "key_themes": ["..."],  
  "summary": "...",
  "sentiment": "Positive/Negative/Neutral",
  "pros": ["..."],
  "cons": ["..."]
}}
"""

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that provides structured JSON outputs."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

result = response.choices[0].message.content
print(result)
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="huggingartists/kizaru",
    task="text-generation",
    )

modal = ChatHuggingFace(llm=llm)

result = modal.invoke("What is the capital of Pkaistan")
print(result.content)


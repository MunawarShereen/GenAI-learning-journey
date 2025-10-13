from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
    
)
model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    
    template="Explain the following question in simple terms: {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    
    template="Explain the following question in 5 bullet point : {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template | model | parser | template2 | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)
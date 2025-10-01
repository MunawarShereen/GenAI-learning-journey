from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate

load_dotenv()
HF_ToKEN = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
)

model = ChatHuggingFace(llm=llm)



template1 = PromptTemplate(
    template="Generate a detailed report on the {topic}.",
    input_variables=["topic"],
)

template2 = PromptTemplate(
    template="Summarize the following report in a 5 lines text:\n{text}",
    input_variables=["text"],
)
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "Pakistan criket team"})

print(result)




    

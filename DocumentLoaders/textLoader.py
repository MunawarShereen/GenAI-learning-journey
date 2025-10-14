from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os


load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Summarize the following content \n {content}",
    input_variables=['content']
)

parser = StrOutputParser()


loader = TextLoader('AI.txt',encoding='utf-8')

docs = loader.load()

# print(type(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'content':docs[0].page_content})

print(result)

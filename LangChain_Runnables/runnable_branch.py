from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableBranch,RunnablePassthrough
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
)

model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template = "Write a deatiled report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Summarize the following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1,model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>200, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_gen_chain,branch_chain)

result = chain.invoke({"topic":"AI"})

print(result)
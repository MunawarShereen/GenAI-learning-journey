from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

llm1 = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
)

model1 = ChatHuggingFace(llm = llm1)


llm2 = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
)

model2 = ChatHuggingFace(llm = llm2)


prompt1 = PromptTemplate(
    template= "Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Generate a LinkedIn post about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet" : RunnableSequence(prompt1,model1,parser),
        "LinkedIn": RunnableSequence(prompt2,model2,parser)
    }
)

result = parallel_chain.invoke({"topic":"AI"})

print(result)
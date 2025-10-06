from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the following joke {text}",
    input_variables=['text']
)
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_cahin = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explain": RunnableSequence(prompt2,model, parser)
    }
)

final_Cahin = RunnableSequence(joke_gen_chain,parallel_cahin)

result = final_Cahin.invoke({"topic":"AI"})

print(result['joke'])






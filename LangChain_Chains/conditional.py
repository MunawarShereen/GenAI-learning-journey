from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableBranch , RunnableParallel, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

HF_ToKEN = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.3-70B-Instruct:cerebras",
    task = "text-generation",
)

model = ChatHuggingFace(llm=llm)

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template="classify the feedback provided by the user as either positive or negative {feedback}.\n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions() }
)

prompt2 = PromptTemplate(
    template="write an appropiate response to the user positive feedback {feedback}.",
    input_variables=["feedback"],
)


prompt3 = PromptTemplate(
    template="write an appropiate response to the user negative feedback {feedback}.",
    input_variables=["feedback"],
)


parser = StrOutputParser()

classifies_chain = prompt | model | parser2

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain =  classifies_chain | branch_chain

result = chain.invoke({"feedback": "The product quality is excellent and I am very satisfied with my purchase!"})

print(result)

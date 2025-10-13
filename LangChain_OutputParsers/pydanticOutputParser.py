from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
import os
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="The person's full name")
    age: int = Field(gt=18 , description="The person's age in years")
    city: str = Field(description="Name of the city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age ad city of fictional {place}.\n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = template | model | parser
result = chain.invoke({"place": "Pakistan"})
print(result)


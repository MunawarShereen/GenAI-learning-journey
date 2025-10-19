from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("FeasibilityReport.pdf")

docs = loader.load()

spliter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)

result = spliter.split_documents(docs)

print(result)


from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("FeasibilityReport.pdf")

docs = loader.load()

print(docs)
print(len(docs))


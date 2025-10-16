from langchain_community.document_loaders import DirectoryLoader, Docx2txtLoader

loader = DirectoryLoader(
    path="Directory",
    glob="*.docx",
    loader_cls=Docx2txtLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
# pip install unstructured[pdf]

from langchain_community.document_loaders import UnstructuredPDFLoader

loader = UnstructuredPDFLoader("")
data = loader.load()
tdata = data[0].page_content
chs = tdata.split(" Chapter")
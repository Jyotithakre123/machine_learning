from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

# Load the dataset
#loader = PyPDFLoader("AIML_Jyoti_thakre.pdf")
loader = PyPDFLoader(r"C:\Users\Jyoti Thakre\Downloads\Python Dictionary  Assignment Question.pdf")

documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, 
                                      chunk_overlap=20)
docs = text_splitter.split_documents(documents)

# Embeddings
embedding = OllamaEmbeddings(model="mxbai-embed-large")

# Vector DB
vectordb = Chroma.from_documents(documents=docs, embedding=embedding)

# Load Ollama model
llm = Ollama(model="deepseek-r1:1.5b")

# Build RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever()
)

# Ask questions
while True:
    query = input("Ask a Question: ")
    if query.lower() == "exit":
        break
    result = qa_chain.invoke({"query": query})
    print(result["result"])



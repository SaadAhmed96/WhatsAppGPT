from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os
from dotenv import load_dotenv

load_dotenv()


# ENV VARIABLES
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")


def load_docs(file_name="./doctors_list.pdf"):
    # Load the pdf
    loader = UnstructuredPDFLoader(file_path=file_name)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    print(f"Now you have {len(texts)} documents")

    return texts


if __name__ == "__main__":
    # initialize pinecone
    pinecone.init(
        api_key=PINECONE_API_KEY,  # find at app.pinecone.io
        environment=PINECONE_API_ENV,  # next to api key in console
    )

    index_name = PINECONE_INDEX_NAME

    print("Pinecone Initialized...")

    # initialize embeddings
    embeddings = OpenAIEmbeddings()
    print("OpenAI Embeddings Initialized...")

    # load docs
    texts = load_docs(file_name="./doctors_list.pdf")
    print("Documents Loaded...")

    # upsert docs to pinecone
    docsearch = Pinecone.from_texts(
        [t.page_content for t in texts], embeddings, index_name=index_name
    )

    print("Upserted Documents..")

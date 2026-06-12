from langchain_chroma import Chroma


def create_vector_store(docs, embedding):

    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory="chroma_db"
    )

    return vectordb
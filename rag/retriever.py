from rag.loader import load_documents
from rag.embedding import get_embedding
from rag.vector_store import create_vector_store

docs = load_documents()

embedding = get_embedding()

db = create_vector_store(
    docs,
    embedding
)

retriever = db.as_retriever()

def retriever_context(query):

    results = retriever.invoke(query)

    context = ""

    for doc in results:
        context += doc.page_content + "\n"

    return context

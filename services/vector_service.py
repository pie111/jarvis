from langchain_chroma import Chroma
from core.config import settings
from services.embedding_service import get_embedding_model

class VectorService:
    def __init__(self, embedding_model: str = settings.DEFAULT_EMBEDDING_MODEL):
        self.embeddings = get_embedding_model(embedding_model)
        self.vector_store = Chroma(
            collection_name="jarvis_collection",
            embedding_function=self.embeddings,
            client_settings={"host": settings.CHROMA_HOST},
        )

    def add_documents(self, documents: list[str]):
        """Add documents to the vector store."""
        self.vector_store.add_texts(texts=documents)
        return {"status": "Documents added"}

    def search(self, query: str, k: int = 3) -> list[str]:
        """Search for similar documents in the vector store."""
        results = self.vector_store.similarity_search(query, k=k)
        return [doc.page_content for doc in results]
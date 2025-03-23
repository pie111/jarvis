from fastapi import APIRouter
from services.llm_service import get_llm
from services.vector_service import VectorService
from core.config import settings

router = APIRouter()


@router.get("/generate")
async def generate_text(provider_model: str = settings.DEFAULT_LLM_MODEL, prompt: str = "Hello, world!"):
    llm = get_llm(provider_model)
    response = llm.invoke(prompt)
    return {"response": response}



@router.post("/vector/add")
async def add_documents(
    documents: list[str],
    embedding_model: str = settings.DEFAULT_EMBEDDING_MODEL
):
    vector_service = VectorService(embedding_model=embedding_model)
    result = vector_service.add_documents(documents)
    return result


@router.get("/vector/search")
async def search_vector(
    query: str,
    embedding_model: str = settings.DEFAULT_EMBEDDING_MODEL,
    k: int = 3
):
    vector_service = VectorService(embedding_model=embedding_model)
    results = vector_service.search(query, k=k)
    return {"results": results}



@router.get("/rag")
async def rag_generate(
    provider_model: str = settings.DEFAULT_LLM_MODEL,
    query: str = "What is AI?",
    embedding_model: str = settings.DEFAULT_EMBEDDING_MODEL,
    k: int = 2
):
    vector_service = VectorService(embedding_model=embedding_model)
    context_docs = vector_service.search(query, k=k)
    context = "\n".join(context_docs)
    
    llm = get_llm(provider_model)
    augmented_prompt = f"Context:\n{context}\n\nQuestion: {query}"
    response = llm.invoke(augmented_prompt)
    return {"response": response, "context": context_docs}
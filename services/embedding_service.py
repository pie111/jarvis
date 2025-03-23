from typing import Union
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from core.config import settings

def get_embedding_model(provider_model: str) -> Union[OpenAIEmbeddings, OllamaEmbeddings]:
    """
    Returns an embedding model instance based on the provider and model specified.
    Example: 'openai/text-embedding-ada-002', 'ollama/nomic-embed-text'.
    
    Args:
        provider_model (str): String in the format 'provider/model'.
    
    Returns:
        An instance of the specified embedding model.
    
    Raises:
        ValueError: If the provider or format is not supported.
    """
    try:
        provider, model = provider_model.split('/')
    except ValueError:
        raise ValueError("Provider/model must be in the format 'provider/model', e.g., 'openai/text-embedding-ada-002'")

    provider = provider.lower()

    if provider == "openai":
        return OpenAIEmbeddings(
            model=model,
            api_key=settings.OPENAI_API_KEY,
        )
    
    elif provider == "ollama":
        return OllamaEmbeddings(
            model=model,
            base_url=settings.OLLAMA_HOST,
        )
    
    else:
        raise ValueError(
            f"Unsupported embedding provider: {provider}. "
            "Supported providers: 'openai', 'ollama'"
        )
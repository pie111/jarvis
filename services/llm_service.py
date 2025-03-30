from typing import Union
from langchain_openai import OpenAI, ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_ibm import WatsonxLLM  # Import Watsonx provider
from core.config import settings


def get_llm(provider_model: str) -> Union[OpenAI, ChatOpenAI, ChatOllama, ChatGroq, WatsonxLLM,ChatGoogleGenerativeAI]:
    """
    Returns an LLM instance based on the provider and model specified.
    Example: 'openai/gpt-4', 'ollama/llama3', 'groq/mixtral-8x7b-32768', 'watsonx/ibm/granite-13b-instruct-v2'.
    
    Args:
        provider_model (str): String in the format 'provider/model'.
    
    Returns:
        An instance of the specified LLM provider.
    
    Raises:
        ValueError: If the provider or format is not supported.
    """
    try:
        provider, model = provider_model.split('/')
    except ValueError:
        raise ValueError("Provider/model must be in the format 'provider/model', e.g., 'openai/gpt-4'")

    provider = provider.lower()

    if provider == "openai":
        if model.startswith("gpt-4") or model.startswith("gpt-3.5"):
            return ChatOpenAI(
                model=model,
                api_key=settings.OPENAI_API_KEY,
                temperature=0.7,
            )
        else:
            return OpenAI(
                model=model,
                api_key=settings.OPENAI_API_KEY,
                temperature=0.7,
            )
    
    elif provider == "ollama":
        return ChatOllama(
            model=model
        )
    
    elif provider == "groq":
        return ChatGroq(
            model=model,
            api_key=settings.GROQ_API_KEY,
            temperature=0.7,
        )
    elif provider == "google":
        print(f"Hey the model is  {model}")
        return ChatGoogleGenerativeAI(
            model=model,
            api_key=settings.GOOGLE_API_KEY
        )
    
    elif provider == "watsonx":
        # Watsonx models like 'ibm/granite-13b-instruct-v2', 'mistralai/mixtral-8x7b-instruct-v01'
        return WatsonxLLM(
            model_id=model,
            url= settings.WATSONX_HOST_URL,  # Adjust based on your region
            apikey=settings.WATSONX_API_KEY,
            project_id=settings.WATSONX_PROJECT_ID,
            params={
                "temperature": 0.7,
                "max_new_tokens": 200,
                "decoding_method": "greedy",
            },
        )
    
    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}. "
            "Supported providers: 'openai', 'ollama', 'groq', 'watsonx'"
        )

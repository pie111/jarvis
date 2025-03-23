from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    API_KEY: str
    MODEL_ENDPOINT: str
    PORT: int = 8000
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST","http://localhost:11434")
    WATSONX_API_KEY: str = os.getenv("WATSONX_API_KEY")  # IBM Cloud API key
    WATSONX_PROJECT_ID: str = os.getenv("WATSONX_PROJECT_ID")  # Watsonx project ID
    WATSONX_HOST_URL: str = os.getenv("WATSONX_HOST_URL", "https://us-south.ml.cloud.ibm.com")  # Adjust based on your region
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    DEFAULT_EMBEDDING_MODEL: str = "ollama/nomic-embed-text:latest"
    CHROMA_HOST: str = os.getenv("CHROMA_HOST", "localhost:8081")
    DEFAULT_LLM_MODEL: str = "ollama/llama3.1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
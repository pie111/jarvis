from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()

class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    API_KEY: str
    MODEL_ENDPOINT: str
    PORT: int = 8000
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST","http://localhost:11434")
    WATSONX_API_KEY: Optional[str] = os.getenv("WATSONX_API_KEY")  # IBM Cloud API key
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    WATSONX_PROJECT_ID: Optional[str] = os.getenv("WATSONX_PROJECT_ID")  # Watsonx project ID
    WATSONX_HOST_URL: Optional[str] = os.getenv("WATSONX_HOST_URL", "https://us-south.ml.cloud.ibm.com")  # Adjust based on your region
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    DEFAULT_EMBEDDING_MODEL: str = "ollama/nomic-embed-text:latest"
    CHROMA_HOST: str = os.getenv("CHROMA_HOST", "localhost:8081")
    DEFAULT_LLM_MODEL: str = os.getenv("DEFAULT_LLM","ollama/llama3.1:8b")
    TAVILY_API_KEY: Optional[str] = os.getenv("TAVILY_API_KEY")
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    ENCRYPTION_KEY: str = os.getenv("ENCRYPTION_KEY", "jarvis")
    DB_POOL_SIZE: int = os.getenv("DB_POOL_SIZE", 5)
    MAX_OVERFLOW: int = os.getenv("MAX_OVERFLOW", 10)

    # MCP settings
    MCP_POSTGRES_CONN_URL : Optional[str] = os.getenv("MCP_POSTGRES_CONN_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
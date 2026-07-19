from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ARENAINTEL"
    API_V1_STR: str = "/api/v1"
    LOG_LEVEL: str = "INFO"
    USE_MOCK_AI: bool = True
    DATABASE_URL: str = "sqlite:///./stadiumops.db"
    
    # Comma-separated list of allowed origins, defaults to local dev
    CORS_ORIGINS: str = "http://localhost:5173,http://127.0.0.1:5173"
    PORT: int = 8000

settings = Settings()

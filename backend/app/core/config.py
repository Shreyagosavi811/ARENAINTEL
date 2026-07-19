from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ARENAINTEL"
    API_V1_STR: str = "/api/v1"
    LOG_LEVEL: str = "INFO"
    USE_MOCK_AI: bool = True
    DATABASE_URL: str = "sqlite:///./stadiumops.db"

settings = Settings()

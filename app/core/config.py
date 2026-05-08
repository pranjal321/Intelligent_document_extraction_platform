
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    GROQ_API_KEY: str = "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"

    DATABASE_URL: str = "sqlite:///./documents.db"

    class Config:
        env_file = ".env"

settings = Settings()

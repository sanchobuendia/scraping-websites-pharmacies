from pydantic import BaseSettings

class Settings(BaseSettings):
    storage_url: str = "./data/"

    class Config:
        env_file = ".env"

settings = Settings()
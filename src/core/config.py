import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_EXPIRE_TIME: int

    ELASTIC_SCHEMA: str
    ELASTIC_HOST: str
    ELASTIC_PORT: str

    LOG_LEVEL: str

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

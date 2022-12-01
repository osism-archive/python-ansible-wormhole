import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    base_url: str = os.getenv("BASE_URL", "http://localhost")


settings = Settings()

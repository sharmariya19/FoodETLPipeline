import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


class Settings:
    API_KEY = os.getenv("API_KEY")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "postgres")


setting = Settings()

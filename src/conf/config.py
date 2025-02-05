import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://admin:admin@localhost:5432/hw8"
    )
    JWT_SECRET = os.getenv("JWT_SECRET", "YOUR_SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_SECONDS = os.getenv("JWT_EXPIRATION_SECONDS", 3600)

    CLD_NAME: str = os.getenv("CLD_NAME", "asdasdasd")
    CLD_API_KEY: int = os.getenv("CLD_API_KEY", 156282568713174)
    CLD_API_SECRET: str = os.getenv("CLD_API_SECRET", "GREGFDGSDSFWEF")


config = Config

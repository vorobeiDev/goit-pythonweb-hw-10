import os


class Config:
    DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://admin:admin@localhost:5432/hw8"
    )
    JWT_SECRET = os.getenv("SECRET_KEY", "YOUR_SECRET_KEY")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_SECONDS = 3600

    CLD_NAME: str = "duumzmt1u"
    CLD_API_KEY: int = 156282568713174
    CLD_API_SECRET: str = "GKkk6Ru45Kg6qFr7RkY6WHlAaOI"


config = Config

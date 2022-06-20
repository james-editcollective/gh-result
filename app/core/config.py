from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = (
        "postgresql://postgres:password@localhost:5432/postgres"
    )

    class Config:
        env_file = ".env"


settings = Settings()

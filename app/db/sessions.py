from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)  # postgresql
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # sqlite
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

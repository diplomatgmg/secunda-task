from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.config import db_config
from database.logging import setup_alchemy_logging


__all__ = ["async_session_factory"]


setup_alchemy_logging()


engine = create_async_engine(db_config.url)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

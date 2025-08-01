from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.config import db_config
from database.logging import setup_alchemy_logging


__all__ = [
    "get_async_session",
    "provide_async_session",
]


setup_alchemy_logging()


engine = create_async_engine(db_config.url)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession]:
    """Контекстный менеджер для работы с базой данных."""
    async with async_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def provide_async_session() -> AsyncGenerator[AsyncSession]:
    """Обёртка над get_async_session, где не поддерживается контекстный менеджер."""
    async with get_async_session() as session:
        yield session

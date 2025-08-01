from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


__all__ = ["Base"]


class Base(DeclarativeBase, AsyncAttrs):
    """Базовый класс для всех моделей."""

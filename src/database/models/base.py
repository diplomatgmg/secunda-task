from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


__all__ = ["Base"]


metadata_obj = MetaData()


class Base(DeclarativeBase, AsyncAttrs):
    """Base class for all models."""

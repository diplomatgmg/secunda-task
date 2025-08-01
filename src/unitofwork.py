from types import TracebackType
from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from database.engine import async_session_factory
from repositories import ActivityRepository, BuildingRepository


__all__ = ["UnitOfWork"]


class UnitOfWork:
    """Конкретная реализация UoW для SQLAlchemy."""

    def __init__(self, session_factory: async_sessionmaker[AsyncSession] = async_session_factory) -> None:
        self._session_factory = session_factory

    async def __aenter__(self) -> Self:
        self._session = self._session_factory()
        self.buildings = BuildingRepository(self._session)
        self.activities = ActivityRepository(self._session)
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        """Сохраняет все изменения в рамках текущей транзакции."""
        await self._session.commit()

    async def rollback(self) -> None:
        """Откатывает все изменения в рамках текущей транзакции."""
        await self._session.rollback()

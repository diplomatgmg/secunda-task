from sqlalchemy.ext.asyncio import AsyncSession


__all__ = ["BaseRepository"]


class BaseRepository:  # noqa: B903
    """Базовый интерфейс репозитория для работы с моделями."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

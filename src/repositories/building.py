from collections.abc import Sequence

from sqlalchemy import select

from database.models import Building
from repositories import BaseRepository


__all__ = ["BuildingRepository"]


class BuildingRepository(BaseRepository):
    """Репозиторий Здания для SQLAlchemy."""

    async def add(self, building: Building) -> Building:
        """Добавляет новое здание в базу данных."""
        self._session.add(building)
        await self._session.flush()

        return building

    async def get(self, building_id: int) -> Building | None:
        """Находит здание по его уникальному идентификатору."""
        result = await self._session.execute(select(Building).where(Building.id == building_id))

        return result.scalar_one_or_none()

    async def get_all(self, skip: int, limit: int) -> Sequence[Building]:
        """Возвращает список зданий с пагинацией."""
        result = await self._session.execute(select(Building).offset(skip).limit(limit))

        return result.scalars().all()

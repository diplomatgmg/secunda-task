from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from database.models import Activity
from repositories import BaseRepository
from repositories.exceptions import TooMuchNestedActivityError


__all__ = ["ActivityRepository"]


class ActivityRepository(BaseRepository):
    """Репозиторий Деятельности для SQLAlchemy."""

    MAX_DEPTH = 3  # Максимальная глубина вложенности

    async def add(self, activity: Activity) -> Activity:
        """Добавляет новую деятельность в базу данных."""
        await self._validate_depth(activity.parent_id)

        self._session.add(activity)
        await self._session.flush()
        await self._session.refresh(activity, ["children"])

        return activity

    async def get(self, activity_id: int) -> Activity | None:
        """Находит деятельность по ID."""
        stmt = select(Activity).where(Activity.id == activity_id)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_ids(self, activity_ids: list[int]) -> Sequence[Activity]:
        """Возвращает список активностей по id."""
        stmt = select(Activity).where(Activity.id.in_(activity_ids))
        result = await self._session.execute(stmt)

        return result.scalars().all()

    async def get_all(self, skip: int, limit: int) -> Sequence[Activity]:
        """Возвращает список деятельностей с пагинацией."""
        stmt = (
            select(Activity)
            .where(Activity.parent_id.is_(None))
            .options(joinedload(Activity.children).joinedload(Activity.children).joinedload(Activity.children))
            .offset(skip)
            .limit(limit)
        )
        result = await self._session.execute(stmt)
        return result.scalars().unique().all()

    async def _validate_depth(self, activity_id: int | None) -> int:
        """Рекурсивно валидирует глубину вложенности деятельности."""
        depth = 1  # Родитель на первом уровне
        current_id: int | None = activity_id

        while current_id is not None:
            # FIXME: N+1 problem
            activity = await self.get(current_id)
            if not activity:
                break
            current_id = activity.parent_id
            depth += 1

        if depth > self.MAX_DEPTH:
            raise TooMuchNestedActivityError(self.MAX_DEPTH)

        return depth

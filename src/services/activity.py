from database.models import Activity
from schemas.activity import ActivityCreate, ActivityRead
from services import BaseService


__all__ = ["ActivityService"]


class ActivityService(BaseService):
    """Слой бизнес-логики для Деятельности."""

    async def create(self, activity_data: ActivityCreate) -> ActivityRead:
        """Создает новую деятельность."""
        async with self._uow:
            activity_model = Activity(
                name=activity_data.name,
                parent_id=activity_data.parent_id,
            )
            created_activity = await self._uow.activities.add(activity_model)
            await self._uow.commit()

            return ActivityRead.model_validate(created_activity)

    async def get_all(self, skip: int, limit: int) -> list[ActivityRead]:
        """Возвращает список деятельностей с пагинацией."""
        async with self._uow:
            activities = await self._uow.activities.get_all(skip, limit)

            return [ActivityRead.model_validate(activity) for activity in activities]

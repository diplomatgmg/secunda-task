from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from api.dependencies import get_activity_service
from schemas.activity import ActivityCreate, ActivityRead
from services import ActivityService


router = APIRouter()


@router.get("/")
async def get_all_activities(
    service: Annotated[ActivityService, Depends(get_activity_service)],
    skip: int = 0,
    limit: int = 100,
) -> Sequence[ActivityRead]:
    """Получить список всех деятельностей."""
    return await service.get_all(skip=skip, limit=limit)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_activity(
    activity_data: ActivityCreate,
    service: Annotated[ActivityService, Depends(get_activity_service)],
) -> ActivityRead:
    """Создать новую деятельность."""
    return await service.create(activity_data)

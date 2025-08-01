from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from api.dependencies import get_building_service
from schemas.building import BuildingCreate, BuildingRead
from services.building import BuildingService


router = APIRouter()


@router.get("/")
async def get_all_buildings(
    service: Annotated[BuildingService, Depends(get_building_service)],
    skip: int = 0,
    limit: int = 100,
) -> Sequence[BuildingRead]:
    """Получить список всех зданий."""
    return await service.get_all(skip=skip, limit=limit)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_building(
    building_data: BuildingCreate,
    service: Annotated[BuildingService, Depends(get_building_service)],
) -> BuildingRead:
    """Эндпоинт для создания нового здания."""
    return await service.create(building_data)

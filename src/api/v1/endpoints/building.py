from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from api.dependencies import get_building_service
from api.v1.endpoints.schemas import BuildingListResponse
from schemas.building import BuildingCreate, BuildingRead
from services.building import BuildingService


router = APIRouter()


@router.get("/")
async def get_all_buildings(
    service: Annotated[BuildingService, Depends(get_building_service)],
    skip: int = 0,
    limit: int = 100,
) -> BuildingListResponse:
    """Получить список всех зданий."""
    buildings = await service.get_all(skip=skip, limit=limit)

    return BuildingListResponse(buildings=buildings)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_building(
    building_data: BuildingCreate,
    service: Annotated[BuildingService, Depends(get_building_service)],
) -> BuildingRead:
    """Создать новое здание."""
    return await service.create(building_data)

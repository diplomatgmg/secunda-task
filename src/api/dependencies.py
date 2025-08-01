from typing import Annotated

from fastapi import Depends

from services import ActivityService, BuildingService
from unitofwork import UnitOfWork


__all__ = [
    "get_activity_service",
    "get_building_service",
]


def get_uow() -> UnitOfWork:
    """Зависимость для получения экземпляра Unit of Work."""
    return UnitOfWork()


def get_building_service(uow: Annotated[UnitOfWork, Depends(get_uow)]) -> BuildingService:
    """FastAPI зависимость для получения экземпляра сервиса BuildingService."""
    return BuildingService(uow)


def get_activity_service(uow: Annotated[UnitOfWork, Depends(get_uow)]) -> ActivityService:
    """FastAPI зависимость для получения экземпляра сервиса ActivityService."""
    return ActivityService(uow)

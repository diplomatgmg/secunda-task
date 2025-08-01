from typing import Annotated

from fastapi import Depends

from services.building import BuildingService
from unitofwork import UnitOfWork


def get_uow() -> UnitOfWork:
    """Зависимость для получения экземпляра Unit of Work."""
    return UnitOfWork()


def get_building_service(uow: Annotated[UnitOfWork, Depends(get_uow)]) -> BuildingService:
    """FastAPI зависимость для получения экземпляра сервиса BuildingService."""
    return BuildingService(uow)

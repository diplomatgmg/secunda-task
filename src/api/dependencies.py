from typing import Annotated

from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from starlette import status

from core.config import app_config
from services import ActivityService, BuildingService, OrganizationService
from unitofwork import UnitOfWork


__all__ = [
    "get_activity_service",
    "get_api_key",
    "get_building_service",
    "get_organization_service",
]


api_key_header = APIKeyHeader(name="X-API-Key")


async def get_api_key(api_key: str = Security(api_key_header)) -> str:  # noqa: RUF029
    """Проверяет переданный API-ключ."""
    if api_key == app_config.api_key:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )


def get_uow() -> UnitOfWork:
    """Зависимость для получения экземпляра Unit of Work."""
    return UnitOfWork()


def get_building_service(uow: Annotated[UnitOfWork, Depends(get_uow)]) -> BuildingService:
    """FastAPI зависимость для получения экземпляра сервиса BuildingService."""
    return BuildingService(uow)


def get_activity_service(uow: Annotated[UnitOfWork, Depends(get_uow)]) -> ActivityService:
    """FastAPI зависимость для получения экземпляра сервиса ActivityService."""
    return ActivityService(uow)


def get_organization_service(uow: Annotated[UnitOfWork, Depends(get_uow)]) -> OrganizationService:
    """FastAPI зависимость для получения экземпляра сервиса OrganizationService."""
    return OrganizationService(uow)

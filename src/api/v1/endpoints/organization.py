from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from api.dependencies import get_organization_service
from schemas.organization import OrganizationCreate, OrganizationRead, PhoneNumberCreate
from services import OrganizationService


router = APIRouter()


@router.get("/")
async def get_all_organizations(
    service: Annotated[OrganizationService, Depends(get_organization_service)],
    skip: int = 0,
    limit: int = 100,
) -> Sequence[OrganizationRead]:
    """Получить список всех организаций."""
    return await service.get_all(skip=skip, limit=limit)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_organization(
    org_data: OrganizationCreate,
    service: Annotated[OrganizationService, Depends(get_organization_service)],
) -> OrganizationRead:
    """Создать новую организацию."""
    return await service.create(org_data)


@router.post("/{organization_id}/phone_numbers")
async def add_phone_number_to_organization(
    organization_id: int,
    phone_data: PhoneNumberCreate,
    service: Annotated[OrganizationService, Depends(get_organization_service)],
) -> OrganizationRead:
    """Добавляет номера телефона к существующей организации."""
    return await service.add_phone_to_organization(org_id=organization_id, phone_number=phone_data.number)

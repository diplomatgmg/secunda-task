from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from api.dependencies import get_organization_service
from api.v1.endpoints.schemas import OrganizationListResponse
from schemas.organization import OrganizationCreate, OrganizationRead
from schemas.phone_number import PhoneNumberCreate
from services import OrganizationService


router = APIRouter()


@router.get("/")
async def get_all_organizations(
    service: Annotated[OrganizationService, Depends(get_organization_service)],
    skip: int = 0,
    limit: int = 100,
) -> OrganizationListResponse:
    """Получить список всех организаций."""
    organizations = await service.get_all(skip=skip, limit=limit)

    return OrganizationListResponse(organizations=organizations)


@router.get("/search/by_name")
async def search_organizations_by_name(
    name: str,
    service: Annotated[OrganizationService, Depends(get_organization_service)],
) -> OrganizationListResponse:
    """Поиск организаций по частичному совпадению имени."""
    organizations = await service.search_by_name(name)

    return OrganizationListResponse(organizations=organizations)


@router.get("/search/by_building/{building_id}")
async def search_organizations_by_building(
    building_id: int,
    service: Annotated[OrganizationService, Depends(get_organization_service)],
) -> OrganizationListResponse:
    """Поиск организаций в конкретном здании."""
    organizations = await service.search_by_building(building_id)

    return OrganizationListResponse(organizations=organizations)


@router.get("/search/by_activity/{activity_id}")
async def search_organizations_by_activity(
    activity_id: int,
    service: Annotated[OrganizationService, Depends(get_organization_service)],
) -> OrganizationListResponse:
    """Поиск организаций по деятельности (включая дочерние)."""
    organizations = await service.search_by_activity_tree(activity_id)

    return OrganizationListResponse(organizations=organizations)


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

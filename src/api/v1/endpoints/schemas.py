from pydantic import BaseModel

from schemas.activity import ActivityRead
from schemas.building import BuildingRead
from schemas.organization import OrganizationRead


__all__ = [
    "ActivityListResponse",
    "BuildingListResponse",
    "OrganizationListResponse",
]


class ActivityListResponse(BaseModel):
    """Схема для ответа со списком деятельностей."""

    activities: list[ActivityRead]


class BuildingListResponse(BaseModel):
    """Схема для ответа со списком зданий."""

    buildings: list[BuildingRead]


class OrganizationListResponse(BaseModel):
    """Схема для ответа со списком организаций."""

    organizations: list[OrganizationRead]

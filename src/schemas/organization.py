from pydantic import BaseModel, ConfigDict

from schemas.activity import ActivityRead
from schemas.building import BuildingRead
from schemas.phone_number import PhoneNumberRead


__all__ = [
    "OrganizationCreate",
    "OrganizationRead",
]


class OrganizationBase(BaseModel):
    """Базовая схема организации."""

    name: str
    building_id: int


class OrganizationCreate(OrganizationBase):
    """Схема для создания организации."""

    phone_numbers: list[str]
    activity_ids: list[int]


class OrganizationRead(OrganizationBase):
    """Схема для чтения организации."""

    id: int
    phone_numbers: list[PhoneNumberRead]
    building: BuildingRead
    activities: list[ActivityRead]

    model_config = ConfigDict(from_attributes=True)

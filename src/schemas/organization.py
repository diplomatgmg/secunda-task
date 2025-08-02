from pydantic import BaseModel, ConfigDict

from schemas.activity import ActivityRead
from schemas.building import BuildingRead


__all__ = [
    "OrganizationCreate",
    "OrganizationRead",
]


class PhoneNumberBase(BaseModel):
    """Базовая схема номера телефона организации."""

    number: str


class PhoneNumberCreate(PhoneNumberBase):
    """Схема для создания номера организации."""


class PhoneNumberRead(PhoneNumberBase):
    id: int
    organization_id: int

    model_config = ConfigDict(from_attributes=True)


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

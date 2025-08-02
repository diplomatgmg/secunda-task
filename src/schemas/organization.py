import re

from pydantic import BaseModel, ConfigDict, field_validator

from schemas.activity import ActivityRead
from schemas.building import BuildingRead
from schemas.exceptions import PhoneNumberPatternError
from schemas.phone_number import PHONE_NUMBER_PATTERN, PhoneNumberRead


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

    @field_validator("phone_numbers")
    @classmethod
    def validate_phone_numbers(cls, numbers: list[str]) -> list[str]:  # noqa: D102
        for number in numbers:
            if not re.match(PHONE_NUMBER_PATTERN, number):
                raise PhoneNumberPatternError
        return numbers


class OrganizationRead(OrganizationBase):
    """Схема для чтения организации."""

    id: int
    phone_numbers: list[PhoneNumberRead]
    building: BuildingRead
    activities: list[ActivityRead]

    model_config = ConfigDict(from_attributes=True)

import re

from pydantic import BaseModel, ConfigDict, field_validator


__all__ = [
    "PhoneNumberCreate",
    "PhoneNumberRead",
]

# 1-234-567 или 1-234-567-89-01
PHONE_NUMBER_PATTERN = r"^(\d-\d\d\d-\d\d\d)(-\d\d-\d\d)?$"


class PhoneNumberBase(BaseModel):
    """Базовая схема номера телефона организации."""

    number: str

    @field_validator("number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(PHONE_NUMBER_PATTERN, value):
            raise ValueError("Номер телефона должен соответствовать формату X-XXX-XXX или X-XXX-XXX-XX-XX")
        return value


class PhoneNumberCreate(PhoneNumberBase):
    """Схема для создания номера телефона организации."""


class PhoneNumberRead(PhoneNumberBase):
    """Схема для чтения номера телефона организации."""

    id: int
    organization_id: int

    model_config = ConfigDict(from_attributes=True)

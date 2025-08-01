from pydantic import BaseModel, ConfigDict, Field


__all__ = [
    "ActivityCreate",
    "ActivityRead",
]


class ActivityBase(BaseModel):
    """Базовая схема для Деятельности."""

    name: str
    parent_id: int | None = Field(None, description="ID родителя")


class ActivityCreate(ActivityBase):
    """Схема для создания Деятельности."""


class ActivityRead(ActivityBase):
    """Схема для чтения данных о Деятельности."""

    id: int

    children: list["ActivityRead"] = []

    model_config = ConfigDict(from_attributes=True)

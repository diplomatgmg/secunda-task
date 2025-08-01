from geoalchemy2 import WKTElement
from geoalchemy2.shape import to_shape
from pydantic import BaseModel, ConfigDict, Field, field_validator


__all__ = [
    "BuildingCreate",
    "BuildingRead",
]


class PointSchema(BaseModel):
    lat: float = Field(..., description="Широта")
    lon: float = Field(..., description="Долгота")


class BuildingBase(BaseModel):
    """Базовая схема для Здания."""

    address: str
    coordinates: PointSchema


class BuildingCreate(BuildingBase):
    """Схема для создания Здания."""


class BuildingRead(BuildingBase):
    """Схема для чтения Здания."""

    id: int

    @field_validator("coordinates", mode="before")
    @classmethod
    def parse_coordinates(cls, value: WKTElement) -> PointSchema:
        """Парсит WKT-строку из PostGIS в объект PointSchema."""
        point = to_shape(value)
        return PointSchema(lat=point.y, lon=point.x)

    model_config = ConfigDict(from_attributes=True)

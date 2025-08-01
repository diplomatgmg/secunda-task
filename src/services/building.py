from geoalchemy2 import WKTElement

from database.models import Building
from schemas.building import BuildingCreate, BuildingRead
from services import BaseService


__all__ = ["BuildingService"]


class BuildingService(BaseService):
    """Слой бизнес-логики для зданий."""

    async def create(self, building_data: BuildingCreate) -> BuildingRead:
        """Создает новое здание."""
        async with self._uow:
            coordinates = WKTElement(
                f"POINT({building_data.coordinates.lon} {building_data.coordinates.lat})", srid=4326
            )

            building_model = Building(
                address=building_data.address,
                coordinates=coordinates,
            )
            created_building = await self._uow.buildings.add(building_model)
            await self._uow.commit()

            return BuildingRead.model_validate(created_building)

    async def get_all(self, skip: int, limit: int) -> list[BuildingRead]:
        """Возвращает список зданий с пагинацией."""
        async with self._uow:
            buildings = await self._uow.buildings.get_all(skip, limit)
            return [BuildingRead.model_validate(building) for building in buildings]

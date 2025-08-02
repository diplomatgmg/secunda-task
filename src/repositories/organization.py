from collections.abc import Sequence

from geoalchemy2 import WKTElement
from geoalchemy2.functions import ST_DWithin
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.orm.interfaces import LoaderOption

from database.models import Activity, Building, Organization
from repositories import BaseRepository


__all__ = ["OrganizationRepository"]


class OrganizationRepository(BaseRepository):
    """Репозиторий для Организации."""

    async def add(self, organization: Organization) -> Organization:
        """Добавляет организацию в базу."""
        self._session.add(organization)
        await self._session.flush()

        return organization

    async def get(self, organization_id: int) -> Organization | None:
        """Получает организацию по id."""
        stmt = select(Organization).where(Organization.id == organization_id).options(*self._default_options)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_name(self, name: str) -> Sequence[Organization]:
        """Ищет организации по частичному совпадению имени."""
        stmt = select(Organization).where(Organization.name.ilike(f"%{name}%")).options(*self._default_options)
        result = await self._session.execute(stmt)

        return result.scalars().all()

    async def get_by_building(self, building_id: int) -> Sequence[Organization]:
        """Ищет организации в конкретном здании."""
        stmt = select(Organization).where(Organization.building_id == building_id).options(*self._default_options)
        result = await self._session.execute(stmt)

        return result.scalars().all()

    async def get_by_activity_ids(self, activity_ids: list[int]) -> Sequence[Organization]:
        """Ищет организации, связанные с любым из перечисленных ID деятельностей."""
        stmt = (
            select(Organization)
            .where(Organization.activities.any(Activity.id.in_(activity_ids)))
            .options(*self._default_options)
        )
        result = await self._session.execute(stmt)

        return result.scalars().unique().all()

    async def get_in_radius(self, lat: float, lon: float, radius_meters: int) -> Sequence[Organization]:
        """Ищет организации в заданном радиусе от точки."""
        search_point = WKTElement(f"POINT({lon} {lat})", srid=4326)

        stmt = (
            select(Organization)
            .join(Building)
            .where(ST_DWithin(Building.coordinates, search_point, radius_meters, use_spheroid=True))
            .options(*self._default_options)
        )
        result = await self._session.execute(stmt)

        return result.scalars().unique().all()

    async def get_all(self, skip: int, limit: int) -> Sequence[Organization]:
        """Получает все организации с пагинацией."""
        stmt = select(Organization).options(*self._default_options).offset(skip).limit(limit)
        result = await self._session.execute(stmt)

        return result.scalars().all()

    @property
    def _default_options(self) -> list[LoaderOption]:
        """Возвращает стандартный набор опций для загрузки связей."""
        return [
            joinedload(Organization.building),
            selectinload(Organization.phone_numbers),
            selectinload(Organization.activities)
            .joinedload(Activity.children)
            .joinedload(Activity.children)
            .joinedload(Activity.children),
        ]

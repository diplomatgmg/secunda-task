from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database.models import Organization
from repositories import BaseRepository


__all__ = ["OrganizationRepository"]


class OrganizationRepository(BaseRepository):
    """Репозиторий для Организации."""

    async def add(self, organization: Organization) -> Organization:
        """Добавляет организацию в базу."""
        self._session.add(organization)
        await self._session.flush()
        await self._session.refresh(organization, ["building"])

        return organization

    async def get(self, organization_id: int) -> Organization | None:
        """Получает организацию по id."""
        stmt = (
            select(Organization)
            .where(Organization.id == organization_id)
            .options(
                selectinload(Organization.phone_numbers),
                selectinload(Organization.building),
                selectinload(Organization.activities),
            )
        )
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all(self, skip: int, limit: int) -> Sequence[Organization]:
        """Получает все организации с пагинацией."""
        stmt = (
            select(Organization)
            .options(
                selectinload(Organization.phone_numbers),
                selectinload(Organization.building),
                selectinload(Organization.activities),
            )
            .offset(skip)
            .limit(limit)
        )
        result = await self._session.execute(stmt)

        return result.scalars().all()

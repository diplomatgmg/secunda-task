from database.models import Organization, PhoneNumber
from schemas.organization import OrganizationCreate, OrganizationRead
from services import BaseService
from services.exceptions import ActivityNotFoundError, OrganizationNotFoundError


__all__ = ["OrganizationService"]


class OrganizationService(BaseService):
    """Слой бизнес-логики для организаций."""

    async def create(self, org_data: OrganizationCreate) -> OrganizationRead:
        """Создает организацию."""
        async with self._uow:
            activities = await self._uow.activities.get_by_ids(org_data.activity_ids)
            for activity in activities:
                if activity.id not in org_data.activity_ids:
                    raise ActivityNotFoundError(activity.id)

            org_model = Organization(
                name=org_data.name,
                building_id=org_data.building_id,
                activities=activities,
                phone_numbers=[PhoneNumber(number=phone) for phone in org_data.phone_numbers],
            )

            created_org = await self._uow.organizations.add(org_model)
            await self._uow.commit()

            return OrganizationRead.model_validate(created_org)

    async def add_phone_to_organization(self, org_id: int, phone_number: str) -> OrganizationRead:
        """Добавляет номер телефона к организации."""
        async with self._uow:
            organization = await self._uow.organizations.get(org_id)
            if not organization:
                raise OrganizationNotFoundError(org_id)

            new_phone = PhoneNumber(number=phone_number)
            organization.phone_numbers.append(new_phone)

            await self._uow.commit()

            return OrganizationRead.model_validate(organization)

    async def get_all(self, skip: int, limit: int) -> list[OrganizationRead]:
        """Возвращает список организаций с пагинацией."""
        async with self._uow:
            organizations = await self._uow.organizations.get_all(skip, limit)
            return [OrganizationRead.model_validate(org) for org in organizations]

    async def search_by_name(self, name: str) -> list[OrganizationRead]:
        """Поиск организаций по имени."""
        async with self._uow:
            organizations = await self._uow.organizations.get_by_name(name)
            return [OrganizationRead.model_validate(org) for org in organizations]

    async def search_by_building(self, building_id: int) -> list[OrganizationRead]:
        """Поиск организаций в здании."""
        async with self._uow:
            organizations = await self._uow.organizations.get_by_building(building_id)
            return [OrganizationRead.model_validate(org) for org in organizations]

    async def search_by_activity_tree(self, activity_id: int) -> list[OrganizationRead]:
        """Поиск организаций по деятельности, включая все дочерние."""
        async with self._uow:
            all_activity_ids = await self._uow.activities.get_all_children_ids(activity_id)
            if not all_activity_ids:
                return []

            organizations = await self._uow.organizations.get_by_activity_ids(list(all_activity_ids))
            return [OrganizationRead.model_validate(org) for org in organizations]

    async def search_in_radius(self, lat: float, lon: float, radius: int) -> list[OrganizationRead]:
        """Поиск организаций в радиусе."""
        async with self._uow:
            organizations = await self._uow.organizations.get_in_radius(lat, lon, radius)
            return [OrganizationRead.model_validate(org) for org in organizations]

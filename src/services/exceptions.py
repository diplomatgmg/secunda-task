__all__ = [
    "ActivityNotFoundError",
    "OrganizationNotFoundError",
]


class ServiceError(Exception):
    """Базовый класс исключений для сервисов."""


class ActivityNotFoundError(ServiceError):
    """Исключение при попытке получить несуществующую активность."""

    def __init__(self, activity_id: int) -> None:
        super().__init__(f"Активности с id: {activity_id} не существует.")


class OrganizationNotFoundError(ServiceError):
    """Исключение при попытке получить несуществующую организацию."""

    def __init__(self, org_id: int) -> None:
        super().__init__(f"Организации с id: {org_id} не существует.")

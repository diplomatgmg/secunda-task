__all__ = ["BuildingDuplicateAddressError"]


class RepositoryError(Exception):
    """Базовый класс исключений для репозиториев."""


class BuildingDuplicateAddressError(RepositoryError):
    """Исключение при попытке создать здание с уже существующим адресом."""

    def __init__(self, address: str) -> None:
        self.address = address
        super().__init__(f"Здание с адресом '{address}' уже существует.")

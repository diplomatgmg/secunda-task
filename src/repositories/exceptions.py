__all__ = [
    "BuildingDuplicateAddressError",
    "TooMuchNestedActivityError",
]


class RepositoryError(Exception):
    """Базовый класс исключений для репозиториев."""


class BuildingDuplicateAddressError(RepositoryError):
    """Исключение при попытке создать здание с уже существующим адресом."""

    def __init__(self, address: str) -> None:
        super().__init__(f"Здание с адресом '{address}' уже существует.")


class TooMuchNestedActivityError(RepositoryError):
    """Исключение при попытке слишком глубокую вложенность деятельности."""

    def __init__(self, max_depth: int) -> None:
        super().__init__(f"Слишком большая вложенность деятельности. Максимальная вложенность: {max_depth}")

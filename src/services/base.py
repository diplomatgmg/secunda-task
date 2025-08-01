from unitofwork import UnitOfWork


__all__ = ["BaseService"]


class BaseService:  # noqa: B903
    """Базовый класс для всех сервисов приложения."""

    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

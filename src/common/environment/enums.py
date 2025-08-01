from enum import StrEnum


__all__ = ["EnvironmentEnum"]


class EnvironmentEnum(StrEnum):
    """Режимы работы/окружения приложения."""

    development = "development"
    production = "production"

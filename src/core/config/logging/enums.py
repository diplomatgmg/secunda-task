from enum import StrEnum


__all__ = ["LogLevel"]


class LogLevel(StrEnum):
    """Возможные уровни логирования."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"

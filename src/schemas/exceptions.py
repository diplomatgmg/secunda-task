__all__ = ["PhoneNumberPatternError"]


class SchemaError(ValueError):
    """Базовый класс исключений при валидации схемы."""


class PhoneNumberPatternError(SchemaError):
    """Исключение при неверном паттерне номера телефона."""

    def __init__(self) -> None:
        super().__init__("Номер телефона должен соответствовать формату X-XXX-XXX или X-XXX-XXX-XX-XX.")

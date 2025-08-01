import logging

from core.config import log_config


__all__ = ["setup_logger"]


def setup_logger() -> None:
    """Инициализирует конфигурацию логгера."""
    logging.basicConfig(
        level=log_config.level.value,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

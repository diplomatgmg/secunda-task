from pydantic_settings import BaseSettings, SettingsConfigDict

from core.config.logging.enums import LogLevel


__all__ = ["log_config"]


class LogConfig(BaseSettings):
    level: LogLevel

    model_config = SettingsConfigDict(env_prefix="LOG_")


log_config = LogConfig()

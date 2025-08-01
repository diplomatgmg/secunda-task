from pydantic_settings import BaseSettings, SettingsConfigDict

from core.config.enums import EnvironmentEnum


__all__ = ["env_config"]


class EnvConfig(BaseSettings):
    """Глобальные настройки окружения."""

    mode: EnvironmentEnum
    project_name: str

    model_config = SettingsConfigDict(env_prefix="ENV_")

    @property
    def debug(self) -> bool:
        return EnvironmentEnum.development == self.mode


env_config = EnvConfig()

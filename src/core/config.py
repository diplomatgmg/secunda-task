from pydantic_settings import BaseSettings, SettingsConfigDict


__all__ = ["app_config"]


class AppConfig(BaseSettings):
    host: str
    port: int

    model_config = SettingsConfigDict(env_prefix="APP_")

app_config = AppConfig()

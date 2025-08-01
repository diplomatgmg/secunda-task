from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


__all__ = ["db_config"]


class DatabaseSettings(BaseSettings):
    host: str = Field("postgis")  # Like docker container name
    port: int
    db: str
    user: str
    password: SecretStr

    model_config = SettingsConfigDict(env_prefix="POSTGRES_")

    @property
    def url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            host=self.host,
            port=self.port,
            database=self.db,
            username=self.user,
            password=self.password.get_secret_value(),
        )


db_config = DatabaseSettings()

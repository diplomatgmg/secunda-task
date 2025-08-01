from pydantic import BaseModel


__all__ = ["HealthResponse"]


class HealthResponse(BaseModel):
    """Ответ на healthcheck."""

    status: str

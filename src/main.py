import logging

from fastapi import FastAPI

from core.config import app_config, env_config
from core.config.logging.factory import setup_logger
from schemas import HealthResponse


__all__ = ["app"]


setup_logger()


logger = logging.getLogger(__name__)

app = FastAPI(
    title=env_config.project_name,
    docs_url="/docs",
    openapi_url="/openapi.json",
)


@app.get("/health", tags=["health"])
async def healthcheck() -> HealthResponse:
    return HealthResponse(status="healthy")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=app_config.host,
        port=app_config.port,
        reload=env_config.debug,
        log_config=None,
    )

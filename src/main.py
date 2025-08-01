from fastapi import FastAPI

from common.environment.config import env_config
from core.config import app_config
from schemas import HealthResponse


__all__ = ["app"]


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
    )

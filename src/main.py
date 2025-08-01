from fastapi import FastAPI

from api.exception_handlers import duplicate_address_handler, too_much_nested_activity_handler
from api.v1.endpoints import router as v1_router
from core.config import app_config, env_config
from core.config.logging.factory import setup_logger
from repositories.exceptions import BuildingDuplicateAddressError, TooMuchNestedActivityError
from schemas.healthcheck import HealthResponse


__all__ = ["app"]


setup_logger()


app = FastAPI(
    title=env_config.project_name,
    docs_url="/docs",
    openapi_url="/openapi.json",
)
app.include_router(v1_router, prefix="/api/v1")

app.add_exception_handler(BuildingDuplicateAddressError, duplicate_address_handler)
app.add_exception_handler(TooMuchNestedActivityError, too_much_nested_activity_handler)


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

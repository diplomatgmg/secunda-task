from fastapi import FastAPI
from fastapi.params import Depends
from starlette import status

from api.dependencies import get_api_key
from api.exception_handlers import (
    create_exception_handler,
)
from api.v1.endpoints import router as v1_router
from core.config import app_config, env_config
from core.config.logging.factory import setup_logger
from repositories.exceptions import BuildingDuplicateAddressError, TooMuchNestedActivityError
from schemas.healthcheck import HealthResponse
from services.exceptions import OrganizationNotFoundError


__all__ = ["app"]


setup_logger()


app = FastAPI(
    title=env_config.project_name,
    docs_url="/docs",
    openapi_url="/openapi.json",
)
app.include_router(v1_router, prefix="/api/v1", dependencies=[Depends(get_api_key)])

app.add_exception_handler(
    BuildingDuplicateAddressError,
    create_exception_handler(status.HTTP_400_BAD_REQUEST),
)
app.add_exception_handler(
    TooMuchNestedActivityError,
    create_exception_handler(status.HTTP_400_BAD_REQUEST),
)
app.add_exception_handler(
    OrganizationNotFoundError,
    create_exception_handler(status.HTTP_404_NOT_FOUND),
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

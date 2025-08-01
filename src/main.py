from fastapi import FastAPI

from common.environment.config import env_config
from core.config import app_config


__all__ = ["app"]


app = FastAPI(
    title=env_config.project_name,
    docs_url="/docs",
    openapi_url="/openapi.json",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=app_config.host,
        port=app_config.port,
        reload=env_config.debug,
    )

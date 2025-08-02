from collections.abc import Callable, Coroutine
import logging
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse


__all__ = ["create_exception_handler"]

logger = logging.getLogger(__name__)


ExceptionHandler = Callable[[Request, Exception], Coroutine[Any, Any, JSONResponse]]


def create_exception_handler(status_code: int) -> ExceptionHandler:
    """Фабрика, создающая обработчики исключений."""

    async def exception_handler(_request: Request, exc: Exception) -> JSONResponse:  # noqa: RUF029
        logger.debug("Handling exception: %s", exc, exc_info=exc)
        return JSONResponse(
            status_code=status_code,
            content={"detail": str(exc)},
        )

    return exception_handler

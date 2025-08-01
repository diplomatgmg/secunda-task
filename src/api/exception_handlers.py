import logging

from fastapi import Request
from fastapi.responses import JSONResponse


__all__ = [
    "duplicate_address_handler",
    "too_much_nested_activity_handler",
]


logger = logging.getLogger(__name__)


async def duplicate_address_handler(  # noqa: RUF029
    _request: Request, exc: Exception
) -> JSONResponse:
    """Обработчик ошибки дублирования адреса здания."""
    logger.debug("Duplicate address: %s", exc)

    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )


async def too_much_nested_activity_handler(  # noqa: RUF029
    _request: Request, exc: Exception
) -> JSONResponse:
    """Обработчик ошибки слишком вложенной деятельности."""
    logger.debug("Too much nested activity: %s", exc)

    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )

from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.core.logger import get_logger


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        log = get_logger()
        log.exception("failed to complete operation", request=request)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error_message": "failed to complete operation internal server error",
                "error_code": "server_error",
            },
        )

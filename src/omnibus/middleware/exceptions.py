from fastapi import Request
from omnibus.log.logger import get_logger


async def add_uncaught_exceptions(request: Request, call_next, exception_return):
    try:
        return await call_next(request)
    except Exception:
        log = get_logger()
        log.exception("failed to complete operation", request=request)
        return exception_return

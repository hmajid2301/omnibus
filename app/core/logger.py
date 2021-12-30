import logging
import logging.config
from typing import Any, Dict

import structlog
import structlog._frames
import uvicorn
import uvicorn.config
from structlog.stdlib import BoundLogger


def setup_logger(log_level: str, env: str):
    _setup_stdlib_logger(log_level=log_level, env=env)
    processors = [
        _add_module_and_lineno,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.TimeStamper("iso"),
    ]
    if env == "production":
        processors.extend(
            [
                structlog.processors.format_exc_info,
                structlog.processors.JSONRenderer(sort_keys=True),
            ]
        )
    else:
        processors.extend(
            [
                structlog.dev.set_exc_info,
                structlog.dev.ConsoleRenderer(),
            ]
        )

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=False,
    )


def _setup_stdlib_logger(log_level: str, env: str):
    logging.getLogger(__name__).setLevel(log_level)
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(),
            },
            "console": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.dev.ConsoleRenderer(),
            },
            **uvicorn.config.LOGGING_CONFIG["formatters"],
        },
        "handlers": {
            "default": {
                "level": log_level,
                "class": "logging.StreamHandler",
                "formatter": "json" if env == "production" else "console",
            },
            "uvicorn.access": {
                "level": log_level,
                "class": "logging.StreamHandler",
                "formatter": "access",
            },
            "uvicorn.default": {
                "level": log_level,
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
        },
        "loggers": {
            "": {"handlers": ["default"], "level": log_level},
            "uvicorn.error": {
                "handlers": ["default" if env == "production" else "uvicorn.default"],
                "level": log_level,
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["default" if env == "production" else "uvicorn.access"],
                "level": log_level,
                "propagate": False,
            },
        },
    }
    logging.config.dictConfig(logging_config)  # type: ignore


def _add_module_and_lineno(logger: structlog.BoundLogger, name: str, event_dict: Dict[str, Any]) -> Dict[str, Any]:
    frame, module_str = structlog._frames._find_first_app_frame_and_name(additional_ignores=[__name__])
    event_dict["module"] = module_str
    event_dict["function"] = frame.f_code.co_name
    event_dict["line"] = frame.f_lineno
    return event_dict


def get_logger() -> BoundLogger:
    log = structlog.get_logger()
    return log

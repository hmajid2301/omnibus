from typing import Any, Callable, Dict, List, Type, Union

from beanie import init_beanie
from beanie.odm.documents import DocType
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_health import health
from motor import motor_asyncio

from omnibus.config.settings import OmnibusSettings
from omnibus.healthcheck import default_healthcheck
from omnibus.log.logger import get_logger, setup_logger


async def setup_app(
    app: FastAPI,
    get_settings: Callable[..., OmnibusSettings],
    document_models: List[Union[Type["DocType"], str]],
    healthcheck: Callable[..., Union[Dict[str, Any], bool]] = default_healthcheck,
):
    config = get_settings()
    setup_logger(log_level=config.LOG_LEVEL, env=config.ENVIRONMENT, uvicorn_log_level=config.UVICORN_LOG_LEVEL)
    uri = config.get_mongodb_uri()
    client = motor_asyncio.AsyncIOMotorClient(uri)
    await init_beanie(database=client[config.DB_NAME], document_models=document_models)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # add_cors(app=app)
    app.add_api_route("/health", health([healthcheck]))

    log = get_logger()
    log.info(f"starting {app.title} {config.WEB_HOST}:{config.WEB_PORT}")

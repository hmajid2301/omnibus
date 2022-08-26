from typing import Any, Callable, Dict, List, Type, Union

from beanie import init_beanie
from beanie.odm.documents import DocType
from beanie.odm.views import View
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
    document_models: List[Union[Type["DocType"], Type["View"], str]],
    healthcheck: Callable[..., Union[Dict[str, Any], bool]] = default_healthcheck,
):
    log = get_logger()
    log.info("HERE")
    config = get_settings()
    setup_logger(log_level=config.LOG_LEVEL, env=config.ENVIRONMENT, uvicorn_log_level=config.UVICORN_LOG_LEVEL)
    log.info("HERE11")
    uri = config.get_mongodb_uri()
    client = motor_asyncio.AsyncIOMotorClient(uri)
    log.info("HERE12", uri=uri)
    await init_beanie(database=client[config.DB_NAME], document_models=document_models)
    log.info("HERE13")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    log.info("HERE14")

    # add_cors(app=app)
    app.add_api_route("/health", health([healthcheck]))

    log.info(f"starting {app.title} {config.WEB_HOST}:{config.WEB_PORT}")

from typing import Any, Callable, Dict, List, Type, Union

from beanie import init_beanie
from beanie.odm.documents import DocType
from fastapi import FastAPI
from fastapi_health import health
from motor import motor_asyncio

from omnibus.config.settings import OmnibusSettings
from omnibus.healthcheck import default_healthcheck
from omnibus.log.logger import get_logger
from omnibus.middleware.cors import add_cors
from omnibus.operation_id import use_route_names_as_operation_ids


async def setup_app(
    app: FastAPI,
    get_settings: Callable[..., OmnibusSettings],
    document_models: List[Union[Type["DocType"], str]] = None,
    healthcheck: Callable[..., Union[Dict[str, Any], bool]] = default_healthcheck,
):
    config = get_settings()
    uri = config.get_mongodb_uri()
    client = motor_asyncio.AsyncIOMotorClient(uri)
    await init_beanie(database=client[config.DB_NAME], document_models=document_models)

    add_cors(app=app, cors=config.CORS, regex_cors=config.REGEX_CORS)
    app.add_api_route("/health", health([healthcheck]))
    use_route_names_as_operation_ids(app)

    log = get_logger()
    log.info(f"starting {app.title} {config.WEB_HOST}:{config.WEB_PORT}")

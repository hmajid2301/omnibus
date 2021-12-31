from typing import Any, Callable, Dict, List, Type, Union

from beanie import init_beanie
from beanie.odm.documents import DocType
from fastapi import FastAPI
from fastapi_health import health
from motor import motor_asyncio

from omnibus.config.settings import get_ominibus_settings
from omnibus.healthcheck import default_healthcheck
from omnibus.middleware.cors import add_cors
from omnibus.middleware.exceptions import add_uncaught_exceptions


async def setup_app(
    document_models: List[Union[Type["DocType"], str]] = None,
    healthcheck: Callable[..., Union[Dict[str, Any], bool]] = default_healthcheck,
) -> FastAPI:
    app = FastAPI()
    config = get_ominibus_settings()
    uri = config.get_mongodb_uri()
    client = motor_asyncio.AsyncIOMotorClient(uri)
    await init_beanie(database=client[config.DB_NAME], document_models=document_models)

    app.middleware("http")(add_uncaught_exceptions)
    add_cors(app=app, cors=config.CORS, regex_cors=config.REGEX_CORS)
    app.add_api_route("/health", health([healthcheck]))
    return app

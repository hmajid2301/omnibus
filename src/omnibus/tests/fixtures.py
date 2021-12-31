import asyncio
from typing import AsyncIterator, List, Type

import pytest
from asgi_lifespan import LifespanManager
from beanie.odm.documents import DocType
from fastapi import FastAPI
from httpx import AsyncClient

from omnibus.app import setup_app


@pytest.fixture()
async def app() -> FastAPI:
    app = await setup_app()
    return app


@pytest.fixture()
async def client(app) -> AsyncIterator[AsyncClient]:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://localhost") as client:
            yield client


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

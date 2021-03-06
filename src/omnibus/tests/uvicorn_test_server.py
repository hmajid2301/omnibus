import asyncio
from typing import Any, Awaitable

import uvicorn
from fastapi.applications import FastAPI


class UvicornTestServer(uvicorn.Server):
    def __init__(self, app: FastAPI, host: str = "127.0.0.1", port: int = 8000):
        self._startup_done = asyncio.Event()
        self._serve_task: Awaitable[Any] | None = None
        super().__init__(config=uvicorn.Config(app, host=host, port=port))

    async def startup(self, sockets: list[Any] | None = None) -> None:
        await super().startup(sockets=sockets)
        self.config.setup_event_loop()
        self._startup_done.set()

    async def start_up(self) -> None:
        self._serve_task = asyncio.create_task(self.serve())
        await self._startup_done.wait()

    async def tear_down(self) -> None:
        self.should_exit = True
        if self._serve_task:
            await self._serve_task

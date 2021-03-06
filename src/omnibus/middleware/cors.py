from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import AnyHttpUrl


def add_cors(app: FastAPI, cors: list[AnyHttpUrl], regex_cors: list[str] | None = None) -> FastAPI:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors,
        allow_origin_regex=regex_cors,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

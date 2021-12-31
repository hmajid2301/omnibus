from typing import List, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import AnyHttpUrl


def add_cors(app: FastAPI, cors: List[AnyHttpUrl], regex_cors: Optional[List[str]] = None) -> FastAPI:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors,
        allow_origin_regex=regex_cors,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

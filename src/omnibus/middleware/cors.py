from fastapi import FastAPI
from pydantic import AnyHttpUrl


def add_cors(app: FastAPI, cors: list[AnyHttpUrl], regex_cors: list[str] | None = None) -> FastAPI:
    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=["*"],
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )
    return app

from pydantic import AnyHttpUrl, BaseSettings


class OmnibusSettings(BaseSettings):
    ENVIRONMENT: str = "production"
    LOG_LEVEL: str = "DEBUG"
    UVICORN_LOG_LEVEL: str = "CRITICAL"

    DB_SCHEMA: str = "mongodb"
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int | None
    DB_NAME: str
    AUTH_DB_NAME: str | None

    WEB_HOST: str = "0.0.0.0"
    WEB_PORT: int = 8080

    CORS: list[AnyHttpUrl] = []
    REGEX_CORS: list[str] | None = None

    CLIENT_ID: str
    USE_AUTH: bool = True

    def get_mongodb_uri(self) -> str:
        uri = f"{self.DB_SCHEMA}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}"
        if self.DB_PORT:
            uri += f":{self.DB_PORT}"
        if self.AUTH_DB_NAME:
            uri += f"?authSource={self.AUTH_DB_NAME}"

        return uri


def get_ominibus_settings():
    return OmnibusSettings()

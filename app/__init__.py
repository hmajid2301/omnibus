import uvicorn

from app.core.config import get_settings
from app.main import application

app = application


if __name__ == "__main__":
    config = get_settings()
    uvicorn.run(application, host=config.WEB_HOST, port=config.WEB_PORT)  # type: ignore

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.api.router import api_router
from src.common.middlewares import ContentTypeMiddleware


def get_app() -> FastAPI:
    """
    Returns the primary instance of the application.
    """
    app = FastAPI(
        title="ProcessDataService",
        version="0.1.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=JSONResponse,
    )

    app.add_middleware(ContentTypeMiddleware)
    app.include_router(api_router)

    return app

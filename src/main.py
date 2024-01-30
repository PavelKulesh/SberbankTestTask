from fastapi import FastAPI

from src.routers.process import process_router
from src.common.middlewares import ContentTypeMiddleware

app = FastAPI(title="ProcessDataService", version="0.1")

app.add_middleware(ContentTypeMiddleware)
app.include_router(process_router)

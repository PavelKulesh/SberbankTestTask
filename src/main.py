import uvicorn
from fastapi import FastAPI

from src.routers.process import process_router
from src.common.middlewares import ContentTypeMiddleware

if __name__ == "__main__":
    app = FastAPI(title="ProcessDataService")

    app.add_middleware(ContentTypeMiddleware)

    app.include_router(process_router, prefix="/api")
    uvicorn.run(app, host="0.0.0.0", port=80)

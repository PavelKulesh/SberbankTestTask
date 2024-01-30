from fastapi import APIRouter

from src.api.v1.router import router_v1

api_router = APIRouter(prefix="/api")
api_router.include_router(router_v1)

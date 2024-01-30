from fastapi import APIRouter

from src.api.v1.documents.router import document_router

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(document_router)

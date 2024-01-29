from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from src.services.json_service import JSONService
from src.services.xml_service import XMLService
from src.common.exceptions import UnsupportedContentType


class ContentTypeMiddleware(BaseHTTPMiddleware):
    service_mapping = {
        "application/json": JSONService(),
        "application/xml": XMLService()
    }

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if content_type := request.headers.get("Content-Type"):
            request.state.service = self.service_mapping.get(content_type)

            if request.state.service is None:
                raise UnsupportedContentType()

            response = await call_next(request)
            return response

        raise UnsupportedContentType()

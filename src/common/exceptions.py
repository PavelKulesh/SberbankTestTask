from fastapi import HTTPException, status


class InvalidDateException(Exception):
    pass


class UnsupportedContentType(HTTPException):
    STATUS_CODE = status.HTTP_422_UNPROCESSABLE_ENTITY
    DEFAULT_MESSAGE = "Unsupported Content Type"

    def __init__(self, message: str | None = None, status_code: int | None = None):
        self.status_code = status_code or self.STATUS_CODE
        self.detail = message or self.DEFAULT_MESSAGE

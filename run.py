import uvicorn
from src.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "src.main:get_app",
        host=settings.host,
        port=settings.port,
        reload=True,
        factory=True,
    )


if __name__ == "__main__":
    main()

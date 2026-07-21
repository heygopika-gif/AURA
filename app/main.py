from fastapi import FastAPI
from app.config import get_settings


def create_app() -> FastAPI:
    """Application factory. All app construction happens here."""
    settings = get_settings()


    app = FastAPI(
        title=settings.app_name,
        description="Personalized AI Life Coach",
        version="0.1.0",
        debug=settings.debug,
    )

    @app.get("/health", tags=["system"])
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Application factory. All app construction happens here."""
    app = FastAPI(
        title="Project Aura",
        description="Personalized AI Life Coach",
        version="0.1.0",
    )

    @app.get("/health", tags=["system"])
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
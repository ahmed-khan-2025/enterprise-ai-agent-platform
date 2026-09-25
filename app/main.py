from fastapi import FastAPI

from app.config import settings
from app.database.database import Base, engine

from app.api.routes import health
from app.api.routes import chat


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)


app.include_router(
    health.router,
    prefix="/api/v1",
)

app.include_router(
    chat.router,
    prefix="/api/v1",
)


@app.get("/")
def root():

    return {
        "application": settings.app_name,
        "status": "running",
    }
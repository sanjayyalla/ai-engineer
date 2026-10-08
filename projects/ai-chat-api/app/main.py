# This is the main FastAPI application file.
# It is the central place where we create the app and include all routers.
# In a real project, this file usually stays small and clean.

from fastapi import FastAPI

from app.routers.chat import router as chat_router
from app.routers.items import router as items_router

# FastAPI app object
app = FastAPI(
    title="AI Chat Practice API",
    version="1.0.0",
    description="A simple learning app covering FastAPI and Pydantic concepts.",
)

# Include all feature routers in the application.
app.include_router(chat_router, prefix="/api/v1")
app.include_router(items_router, prefix="/api/v1")


@app.get("/health")
def health_check() -> dict[str, str]:
    # A simple health endpoint to confirm the app is running.
    return {"status": "healthy"}

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router

app = FastAPI(
    title="ComicCraft",
    description="AI Comic Story Creator using Gemini Models",
    version="1.0.0"
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Routes
app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status": "success",
        "message": "ComicCraft API is running"
    }
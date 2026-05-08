
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Intelligent Document Extraction Platform")

app.include_router(router)

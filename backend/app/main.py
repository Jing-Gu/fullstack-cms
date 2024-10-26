from fastapi import FastAPI
from app.api.v1.main import api_router_v1

app = FastAPI(title="Content Management API")

app.include_router(api_router_v1, prefix="/api/v1")

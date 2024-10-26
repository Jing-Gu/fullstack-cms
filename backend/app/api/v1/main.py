from fastapi import APIRouter

from app.api.v1.routers import portfolios

api_router_v1 = APIRouter()
api_router_v1.include_router(portfolios.router, prefix="/portfolios", tags=["portfolios"])
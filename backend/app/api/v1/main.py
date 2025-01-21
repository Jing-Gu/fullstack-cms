from fastapi import APIRouter
from app.api.v1.routers import portfolios
from app.api.v1.routers import news

api_router_v1 = APIRouter()
api_router_v1.include_router(portfolios.router, prefix="/portfolios", tags=["portfolios"])
api_router_v1.include_router(news.router, prefix="/news", tags=["news"])

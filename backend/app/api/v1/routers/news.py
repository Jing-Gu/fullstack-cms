from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from datetime import date
from app.api.v1.database.db import get_news_from_json, save_news_to_json, save_news_list_to_json, get_news_by_id_from_json
import logging
import uuid

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NewsItem(BaseModel):
    title: str
    editor: str
    fileUpload: bytes
    startDate: date
    endDate: date
    displayDate: date
    createdAt: date
    requestedBy: str
    draft: bool


class NewsUpdate(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    editor: Optional[str] = None
    fileUpload: Optional[bytes] = None
    startDate: Optional[date] = None
    endDate: Optional[date] = None
    displayDate: Optional[date] = None
    draft: Optional[bool] = None


@router.get("/")
async def get_news():
    return get_news_from_json()


@router.get("/{news_id}")
async def get_news_by_id(news_id: str):
    try:
        news = get_news_by_id_from_json(news_id)
        if news:
            return news
        raise HTTPException(status_code=404, detail=f"News {news_id} not found")
    except Exception as e:
        logger.error(f"Error fetching news with ID {news_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.patch("/{news_id}")
async def update_news_by_id(news_id: str, news: dict):
    logger.info(f"Updating news with ID {news_id}")
    try:
        news_item = get_news_by_id_from_json(news_id)
        if not news_item:
            raise HTTPException(status_code=404, detail=f"News {news_id} not found")
        # Update only the provided fields
        news_item.update(news)
        save_news_to_json(news_item)
        return {"message": "News updated successfully", "news": news_item}
    except Exception as e:
        logger.error(f"Error updating news with ID {news_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete("/{news_id}")
async def delete_news_by_id(news_id: str):
    logger.info(f"Deleting news with ID {news_id}")
    try:
        news_list = get_news_from_json()
        for i, news in enumerate(news_list):
            if news['id'] == news_id:
                del news_list[i]
                save_news_list_to_json(news_list)
                return {"message": "News deleted successfully"}
        raise HTTPException(status_code=404, detail=f"News {news_id} not found")
    except Exception as e:
        logger.error(f"Error deleting news with ID {news_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/")
async def create_news(news: dict): # BUG: why NewsItem pydantic model does not work, error 422
    logger.info(f"Creating news: {news.get('title')}")
    try:
        news['id'] = str(uuid.uuid4())
        save_news_to_json(news)
        return {"message": "News created successfully"}
    except Exception as e:
        logger.error(f"Error creating news: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.patch("/")
async def update_news_order(upd_news_list: list[dict]):
    logger.info(f"Updating news order")
    try:
        news_list = get_news_from_json()

        # Update the order based on the provided list
        for item in upd_news_list:
            news_id = item.get('id')
            new_order = item.get('order')
            for news in news_list:
                if news['id'] == news_id:
                    news['order'] = new_order
                    logger.info(f"Updated order for news ID {news_id} to {new_order}")
                    break
            else:
                logger.warning(f"News with ID {news_id} not found")
                raise HTTPException(status_code=404, detail=f"News with ID {news_id} not found")
        
        # Save the updated list
        save_news_list_to_json(news_list)
        
        return {"message": "News order updated successfully", "news": news_list}
    except Exception as e:
        logger.error(f"Error updating news order: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


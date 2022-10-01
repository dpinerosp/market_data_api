"""Market Data Route for /news/historical endpoint."""
from typing import List

from fastapi import APIRouter
from schemas.news import News
from services.news import historical

router = APIRouter(prefix="/news", tags=["news"])


@router.get(path="/historical/", response_model=List[News])
def get_historical_news(
    ticker: str,
) -> List[News]:
    return historical.get_historical_news(ticker=ticker)

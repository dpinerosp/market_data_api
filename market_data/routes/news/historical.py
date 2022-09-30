"""Market Data Route for /news/historical endpoint."""
from fastapi import APIRouter
from schemas.news import News

router = APIRouter()


@router.post(path="/news/historical/", response_model=News, tags=["news"])
async def get_historical_news(
    ticker: str,
) -> News:
    return News(
        updated_at="08/15/2022 11:30:05",
        headline="This is an important news",
        image="https://example.com/this-is-an-image",
        source="danilopineros.com",
        summary="This is the summary of the important news",
    )

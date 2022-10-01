"""Market Data Historical News service."""
from datetime import datetime
from typing import List

from schemas.news import News


def get_historical_news(ticker: str) -> List[News]:
    """Return"""
    return [
        News(
            updated_at=datetime.strptime(
                "08/15/2022 11:30:05", "%m/%d/%Y %H:%M:%S"
            ),
            headline="This is an important news",
            image="https://example.com/this-is-an-image",
            source="danilopineros.com",
            summary="This is the summary of the important news",
        )
    ]

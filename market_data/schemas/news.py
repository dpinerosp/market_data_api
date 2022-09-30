"""Market Data News schema."""
from datetime import datetime

from pydantic import BaseModel


class News(BaseModel):
    """Base schema definition of News."""

    updated_at: datetime
    headline: str
    image: str
    source: str
    summary: str

    class Config:
        """Example of schema for News."""

        schema_extra = {
            "example": {
                "updated_at": "08/15/2022 11:30:05",
                "headline": "This is an important news",
                "image": "https://example.com/this-is-an-image",
                "source": "danilopineros.com",
                "summary": "This is the summary of the important news",
            }
        }

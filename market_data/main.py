"""Market Data main."""
from fastapi import FastAPI
from routes.news import historical
from starlette.middleware.cors import CORSMiddleware

# Create market_data instance
market_data = FastAPI(
    title="Market Data",
    description="Market Data Api",
    contact={
        "name": "Danilo Piñeros",
        "url": "https://danilopineros.com",
        "email": "dspinerosp@gmail.com",
    },
)

# Add middlewares
market_data.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


market_data.include_router(historical.router)

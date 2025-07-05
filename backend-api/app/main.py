from fastapi import FastAPI
from app.endpoints import health, predict  # Make sure predict is included

app = FastAPI()
app.include_router(health.router)
app.include_router(predict.router)  # This line is CRITICAL!

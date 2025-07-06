from fastapi import FastAPI
from app.endpoints import health

app = FastAPI()
app.include_router(health.router)

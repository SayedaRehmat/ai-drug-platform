# backend-api/app/main.py
from fastapi import FastAPI
from endpoints import health, predict

app = FastAPI()
app.include_router(health.router)
app.include_router(predict.router)

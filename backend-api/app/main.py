from fastapi import FastAPI
from app.endpoints import health, predict  # add predict

app = FastAPI()
app.include_router(health.router)
app.include_router(predict.router)  # include new router

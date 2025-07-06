from fastapi import FastAPI
from app.endpoints import health, predict  # ← Make sure this line is here

app = FastAPI()

# Include both routers
app.include_router(health.router)
app.include_router(predict.router)

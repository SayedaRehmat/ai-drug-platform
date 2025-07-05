from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
import subprocess
import json

router = APIRouter()

class PredictionInput(BaseModel):
    compound: str
    protein: str

@router.post("/predict")
def predict(input: PredictionInput) -> Dict:
    # Call dummy predictor from ml-engine
    # Simulate prediction for now
    score = 0.85
    return {
        "compound": input.compound,
        "protein": input.protein,
        "binding_score": score
    }

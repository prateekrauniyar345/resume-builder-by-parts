from pydantic import BaseModel
from fastapi import APIRouter
import datetime


default_router = APIRouter(prefix="/api", tags=["default"])



@default_router.get("/")
def home():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the Resume Optimizer API!.",
        "Date": datetime.datetime.now(),
        "status": "API is running",
    }
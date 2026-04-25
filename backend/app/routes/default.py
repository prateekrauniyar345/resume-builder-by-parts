"""
Default routes for the Resume Optimizer API.
Provides health check endpoints.
"""

from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

default_router = APIRouter(prefix="/api", tags=["default"])



@default_router.get("/backend-health")
def home():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the Resume Optimizer API!",
        "timestamp": datetime.now().isoformat(),
        "status": "API is running",
        "docs_url": "/docs",
    }
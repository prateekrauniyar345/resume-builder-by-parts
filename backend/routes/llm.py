from pydantic import BaseModel
from fastapi import APIRouter
from datetime import datetime
import os
import time


llm_router = APIRouter(prefix="/api", tags=["health"])

class LLMHealthRespose(BaseModel):
    status: str
    message: str
    latency_ms: float
    timestamp: str
    provider: str
    model: str


@llm_router.get("/llm-health", response_model=LLMHealthRespose)
def llm_health_response():
    provider = os.getenv("LLM_PROVIDER", "cerebras").lower()
    model = os.getenv("LLM_MODEL", "unknown")
    api_key = os.getenv("LLM_API_KEY")


    if model == "unknown":
        return LLMHealthRespose(
            status="unhealthy",
            message="LLM_MODEL environment variable not set",
            latency_ms=0,
            timestamp=datetime.now().isoformat(),
            provider=provider,
            model=model,
        )

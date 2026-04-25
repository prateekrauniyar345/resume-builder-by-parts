import os
import time
from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
from app.agents.get_llm import get_llm
from app.models import LLMHealthResponse, LLMProviderInfo

load_dotenv()

llm_router = APIRouter(prefix="/api", tags=["health"])


@llm_router.get("/llm-provider", response_model=LLMProviderInfo)
async def llm_provider_info():
    return LLMProviderInfo(
        provider=os.getenv("LLM_PROVIDER", "UNKNOWN").lower(),
        model=os.getenv("LLM_MODEL", "UNKNOWN"),
    )


@llm_router.get("/llm-health", response_model=LLMHealthResponse)
async def llm_health_check():
    start_time = time.time()
    provider = os.getenv("LLM_PROVIDER", "UNKNOWN").lower()
    model = os.getenv("LLM_MODEL", "UNKNOWN")

    try:
        llm = get_llm()
        # All providers now use LangChain's unified interface
        response = llm.invoke("Respond with only the word: ok")
        response_text = getattr(response, "content", str(response)).strip()

        latency_ms = (time.time() - start_time) * 1000

        return LLMHealthResponse(
            status="healthy",
            message=f"LLM is responding normally. Response: {response_text}",
            latency_ms=round(latency_ms, 2),
            timestamp=datetime.now().isoformat(),
            provider=provider,
            model=model,
        )

    except Exception as e:
        latency_ms = (time.time() - start_time) * 1000
        return LLMHealthResponse(
            status="unhealthy",
            message=f"LLM health check failed: {str(e)}",
            latency_ms=round(latency_ms, 2),
            timestamp=datetime.now().isoformat(),
            provider=provider,
            model=model,
        )
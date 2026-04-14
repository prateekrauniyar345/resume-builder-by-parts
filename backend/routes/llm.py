"""
Health check routes for the Resume Optimizer API.
Includes API health status and LLM agent health monitoring.
"""

from http import client

from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import time
from google import genai
import os
from dotenv import load_dotenv

# load the .env file
load_dotenv()

# Create router
llm_router = APIRouter(prefix="/api", tags=["health"])


class LLMHealthResponse(BaseModel):
    """Response model for LLM health check."""
    status: str
    message: str
    latency_ms: float
    timestamp: str
    provider: str
    model: str


class LLMProviderInfo(BaseModel):
    """Model for LLM provider information."""
    provider: str
    model: str


@llm_router.get("/llm-provider", response_model=LLMProviderInfo)
async def llm_provider_info():
    return LLMProviderInfo(
            provider=os.getenv("LLM_PROVIDER", "UNKNOWN").lower(),
            model=os.getenv("LLM_MODEL", "UNKNOWN"),
        )

@llm_router.get("/llm-health", response_model=LLMHealthResponse)
async def llm_health_check():
    """
    Check the health and latency of the LLM.
    Directly invokes the LLM to test connectivity and response time.
    Returns:
        LLMHealthResponse with status, message, latency_ms, timestamp, provider, and model
    """
    start_time = time.time()
    
    try:
        # Get LLM API key
        api_key = os.getenv("LLM_API_KEY", "")
        print("llm api key is : {}".format(api_key))
        model = os.getenv("LLM_MODEL", "UNKNOWN")
        print("llm model is : {}".format(model))
        if not api_key:
            end_time = time.time()
            latency_ms = (end_time - start_time) * 1000
            return LLMHealthResponse(
                status="unhealthy",
                message="LLM_API_KEY environment variable not set",
                latency_ms=round(latency_ms, 2),
                timestamp=datetime.now().isoformat(),
                provider=os.getenv("LLM_PROVIDER", "UNKNOWN").lower(),
                model=model,
            )


        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents="Reply with only the word: OK"
        )
        
        # Calculate latency
        end_time = time.time()
        latency_ms = (end_time - start_time) * 1000
        
        return LLMHealthResponse(
            status="healthy",
            message=f"LLM is responding normally. Response: {response.text}",
            latency_ms=round(latency_ms, 2),
            timestamp=datetime.now().isoformat(),
            provider=os.getenv("LLM_PROVIDER", "UNKNOWN").lower(),
            model=model,
        )
        
    except Exception as e:
        end_time = time.time()
        latency_ms = (end_time - start_time) * 1000
        
        return LLMHealthResponse(
            status="unhealthy",
            message=f"LLM health check failed: {str(e)}",
            latency_ms=round(latency_ms, 2),
            timestamp=datetime.now().isoformat(),
            provider=os.getenv("LLM_PROVIDER", "UNKNOWN").lower(),
            model=model,
        )

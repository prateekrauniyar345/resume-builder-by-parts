"""
Health check routes for the Resume Optimizer API.
Includes API health status and LLM agent health monitoring.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import time
from langchain_cerebras import ChatCerebras
from langchain_core.messages import HumanMessage

# Create router
router = APIRouter(prefix="", tags=["health"])


class LLMHealthResponse(BaseModel):
    """Response model for LLM health check."""
    status: str
    message: str
    latency_ms: float
    timestamp: str
    provider: str
    model: str


@router.get("/")
def home():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the Resume Optimizer API!.",
        "Date": datetime.now(),
        "status": "API is running",
    }


@router.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "Resume Optimizer API is running"}


@router.get("/llm-health", response_model=LLMHealthResponse)
async def llm_health_check():
    """
    Check the health and latency of the Cerebras LLM.
    Directly invokes the LLM to test connectivity and response time.

    Returns:
        LLMHealthResponse with status, message, latency_ms, timestamp, provider, and model
    """
    import os
    
    start_time = time.time()
    
    try:
        # Get Cerebras API key
        api_key = os.getenv("CEREBRAS_API_KEY")
        if not api_key:
            end_time = time.time()
            latency_ms = (end_time - start_time) * 1000
            return LLMHealthResponse(
                status="unhealthy",
                message="CEREBRAS_API_KEY environment variable not set",
                latency_ms=round(latency_ms, 2),
                timestamp=datetime.now().isoformat(),
                provider="cerebras",
                model="llama-3.1-70b",
            )
        
        # Initialize Cerebras LLM
        llm = ChatCerebras(
            api_key=api_key,
            model="llama-3.1-70b",
        )
        
        # Send a simple test message
        response = llm.invoke([HumanMessage(content="Respond with only the word: ok")])
        
        # Calculate latency
        end_time = time.time()
        latency_ms = (end_time - start_time) * 1000
        
        return LLMHealthResponse(
            status="healthy",
            message=f"Cerebras LLM is responding normally. Response: {response.content}",
            latency_ms=round(latency_ms, 2),
            timestamp=datetime.now().isoformat(),
            provider="cerebras",
            model="llama-3.1-70b",
        )
        
    except Exception as e:
        end_time = time.time()
        latency_ms = (end_time - start_time) * 1000
        
        return LLMHealthResponse(
            status="unhealthy",
            message=f"Cerebras LLM health check failed: {str(e)}",
            latency_ms=round(latency_ms, 2),
            timestamp=datetime.now().isoformat(),
            provider="cerebras",
            model="llama-3.1-70b",
        )

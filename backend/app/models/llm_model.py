from pydantic import BaseModel

class LLMHealthResponse(BaseModel):
    status: str
    message: str
    latency_ms: float
    timestamp: str
    provider: str
    model: str


class LLMProviderInfo(BaseModel):
    provider: str
    model: str
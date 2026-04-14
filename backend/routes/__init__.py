from .health import health_router
from .resume import resume_router
from .llm import llm_router
from .default import default_router 


__all__ = [
    "health_router",
    "resume_router",
    "llm_router",
    "default_router",
]
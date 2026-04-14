"""
FastAPI server for resume optimization using multi-agent CrewAI system.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import  resume_router, llm_router, default_router
import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Resume Optimizer API",
    description="Multi-agent system for optimizing resumes based on job descriptions",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the Resume Optimizer API!.",
        "Date": datetime.datetime.now(),
        "status": "API is running",
    }

# Register routers
app.include_router(resume_router)
app.include_router(llm_router)
app.include_router(default_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

"""
FastAPI server for resume optimization using multi-agent CrewAI system.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from pathlib import Path

from backend.agents import ResumeOptimizationCrew, ResumeLoader, ResumeBuilder

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


# Request/Response models
class ResumeOptimizationRequest(BaseModel):
    """Request model for resume optimization."""
    job_description: str
    job_title: Optional[str] = "Optimized Position"


class ResumeOptimizationResponse(BaseModel):
    """Response model for resume optimization."""
    status: str
    message: str
    resume_content: str
    file_path: str
    filename: str


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "Resume Optimizer API is running"}


@app.post("/optimize-resume", response_model=ResumeOptimizationResponse)
async def optimize_resume(request: ResumeOptimizationRequest):
    """
    Optimize resume based on job description.
    
    Args:
        request: ResumeOptimizationRequest with job_description and optional job_title
        
    Returns:
        ResumeOptimizationResponse with optimized resume content and file path
    """
    try:
        # Validate job description
        if not request.job_description or len(request.job_description.strip()) < 50:
            raise HTTPException(
                status_code=400,
                detail="Job description must be at least 50 characters long",
            )

        # Load candidate context
        loader = ResumeLoader()
        context = loader.create_context()

        # Create and run the optimization crew
        crew = ResumeOptimizationCrew(
            job_description=request.job_description,
            resume_context=context,
        )

        optimized_sections = crew.optimize()

        # Build and save the resume
        builder = ResumeBuilder()
        result = builder.generate_and_save(
            job_title=request.job_title,
            optimized_sections=optimized_sections,
        )

        return ResumeOptimizationResponse(
            status="success",
            message=f"Resume successfully optimized for {request.job_title}",
            resume_content=result["content"],
            file_path=result["file_path"],
            filename=result["filename"],
        )

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error optimizing resume: {str(e)}",
        )


@app.get("/resume-parts")
def get_resume_parts():
    """Get all current resume parts for reference."""
    try:
        loader = ResumeLoader()
        parts = loader.load_all_resume_parts()
        return {
            "status": "success",
            "parts": {k: v[:200] + "..." if len(v) > 200 else v for k, v in parts.items()},
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error loading resume parts: {str(e)}",
        )


@app.get("/output-directory")
def get_output_directory():
    """Get the output directory path."""
    output_dir = Path(__file__).parent / "output"
    return {
        "status": "success",
        "output_directory": str(output_dir),
        "absolute_path": str(output_dir.absolute()),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

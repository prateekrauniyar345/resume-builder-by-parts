"""
Resume optimization routes for the Resume Optimizer API.
Handles resume optimization, parts retrieval, and output management.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from pathlib import Path

from app.agents import ResumeOptimizationCrew, ResumeLoader, ResumeBuilder

# Create router
router = APIRouter(prefix="", tags=["resume"])


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


@router.post("/optimize-resume", response_model=ResumeOptimizationResponse)
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


@router.get("/resume-parts")
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


@router.get("/output-directory")
def get_output_directory():
    """Get the output directory path."""
    output_dir = Path(__file__).parent.parent / "output"
    return {
        "status": "success",
        "output_directory": str(output_dir),
        "absolute_path": str(output_dir.absolute()),
    }

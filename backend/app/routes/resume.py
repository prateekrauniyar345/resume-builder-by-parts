from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.workflow import resume_workflow
from typing import Dict, Optional, List, Tuple, Union
import os


resume_router = APIRouter(prefix="/resume", tags=["resume"])


@resume_router.post("/optimize-resume", response_model=dict)
def optimize_resume(
    job_description: str, 
    job_name: Optional[str] = None,
    resume_context: Optional[Dict] = None
):
    """
    Endpoint to optimize resume based on job description, job name, and current resume context.
    """
    if not job_description:
        raise HTTPException(status_code=400, detail="Job description is required.")
    
    # Initialize state
    initial_state = {
        "job_description": job_description,
        "job_name": job_name,
        "resume_context": resume_context or {},
        "optimized_sections": {},
        "judge_feedback": "",
    }
    
    # Run the workflow
    # result = resume_workflow.run(initial_state)
    
    return {
        "optimized_sections": result.get("optimized_sections", {}),
        "judge_feedback": result.get("judge_feedback", ""),
    }
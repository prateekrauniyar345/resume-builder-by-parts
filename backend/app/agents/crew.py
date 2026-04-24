"""
Resume optimization agents using LangChain and LangGraph.
(Migrating from CrewAI - agents TBD)

This file will be replaced with LangChain/LangGraph implementation.
System prompts are preserved in config.py for future use.
"""

import os
import sys
from dotenv import load_dotenv

from ..prompts import (
    SKILLS_AGENT_SYSTEM_PROMPT,
    EDUCATION_AGENT_SYSTEM_PROMPT,
    EXPERIENCE_AGENT_SYSTEM_PROMPT,
    PROJECTS_AGENT_SYSTEM_PROMPT,
)
from .llm_config import get_llm
import re

load_dotenv()

# Get model configuration from environment
_provider = os.getenv("LLM_PROVIDER", "genai").lower().strip()
_model = os.getenv("LLM_MODEL", "gemini-2.5-flash-lite").strip()
_api_key = os.getenv("LLM_API_KEY", "").strip()


def _clean_latex_output(text: str) -> str:
    r"""
    Clean LaTeX output by removing markdown code blocks, document preamble, and duplicate content.
    
    Extracts only the section-specific LaTeX content (e.g., \vspace...\section*...\itemize...\end{itemize}).
    Removes markdown code blocks (```latex ... ```), \documentclass, \usepackage, etc.
    """
    if not text:
        return ""
    
    # Remove markdown code blocks (```latex ... ```)
    text = re.sub(r'```latex\s*(.*?)\s*```', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'```\s*(.*?)\s*```', r'\1', text, flags=re.DOTALL)
    
    # Remove document preamble elements
    text = re.sub(r'\\documentclass\[.*?\]\{.*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\usepackage(?:\[.*?\])?\{.*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{document\}', '', text)
    text = re.sub(r'\\end\{document\}', '', text)
    
    # Remove duplicate \end{document} tags
    while '\\end{document}' in text:
        text = text.replace('\\end{document}', '')
    
    # Remove common preamble formatting commands at document level
    text = re.sub(r'\\pagestyle\{.*?\}', '', text)
    text = re.sub(r'\\setlength.*?\n', '', text)
    text = re.sub(r'\\hypersetup\{.*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\titleformat.*?\]', '', text, flags=re.DOTALL)
    
    # Remove leading/trailing whitespace and extra newlines
    text = text.strip()
    text = re.sub(r'\n\n\n+', '\n\n', text)  # Remove excessive newlines
    
    return text


class ResumeOptimizationCrew:
    """
    Resume optimization orchestrator.
    
    PLACEHOLDER: Currently returns original sections unchanged.
    To be replaced with LangChain/LangGraph implementation.
    
    System prompts are preserved in config.py for future use:
    - SKILLS_AGENT_SYSTEM_PROMPT
    - EDUCATION_AGENT_SYSTEM_PROMPT
    - EXPERIENCE_AGENT_SYSTEM_PROMPT
    - PROJECTS_AGENT_SYSTEM_PROMPT
    """

    def __init__(self, job_description: str, resume_context: dict):
        """
        Initialize the optimizer with job description and resume context.
        
        Args:
            job_description: The target job posting
            resume_context: Dictionary containing current resume sections and candidate info
        """
        self.job_description = job_description
        self.resume_context = resume_context
        self.llm = get_llm()

    def optimize(self) -> dict:
        """
        Placeholder for resume optimization.
        
        Currently returns original sections unchanged.
        To be replaced with LangChain/LangGraph implementation.
        
        Returns:
            Dictionary with optimized sections (currently unchanged)
        """
        print("[INFO] Using placeholder optimization (CrewAI removed - LangChain/LangGraph implementation pending)", file=sys.stderr)
        
        # Placeholder: return original sections unchanged for now
        optimized_sections = {
            "skills": self.resume_context.get("skills", ""),
            "education": self.resume_context.get("education", ""),
            "experience": self.resume_context.get("experience", ""),
            "projects": self.resume_context.get("projects", ""),
        }
        
        return optimized_sections

"""
Resume Builder Application Package.
Contains agents, prompts, and utilities for resume optimization.
"""

from .prompts import (
    SKILLS_AGENT_SYSTEM_PROMPT,
    EDUCATION_AGENT_SYSTEM_PROMPT,
    EXPERIENCE_AGENT_SYSTEM_PROMPT,
    PROJECTS_AGENT_SYSTEM_PROMPT,
)

__all__ = [
    "SKILLS_AGENT_SYSTEM_PROMPT",
    "EDUCATION_AGENT_SYSTEM_PROMPT",
    "EXPERIENCE_AGENT_SYSTEM_PROMPT",
    "PROJECTS_AGENT_SYSTEM_PROMPT",
]

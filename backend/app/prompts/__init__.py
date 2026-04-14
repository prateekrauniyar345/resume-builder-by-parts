"""
System prompts for all resume optimization agents.
Each agent has a specialized prompt for optimizing different resume sections.
"""

from .skills_agent_prompt import SKILLS_AGENT_SYSTEM_PROMPT
from .education_agent_prompt import EDUCATION_AGENT_SYSTEM_PROMPT
from .experience_agent_prompt import EXPERIENCE_AGENT_SYSTEM_PROMPT
from .projects_agent_prompt import PROJECTS_AGENT_SYSTEM_PROMPT

__all__ = [
    'SKILLS_AGENT_SYSTEM_PROMPT',
    'EDUCATION_AGENT_SYSTEM_PROMPT',
    'EXPERIENCE_AGENT_SYSTEM_PROMPT',
    'PROJECTS_AGENT_SYSTEM_PROMPT',
]

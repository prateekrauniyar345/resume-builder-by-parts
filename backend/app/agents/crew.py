"""
Resume optimization agents using CrewAI.
Each agent specializes in a specific resume section.
"""

import os
import sys
from crewai import Agent, Task, Crew
from crewai.llm import LLM
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

# Set up environment for CrewAI to recognize Gemini
if not os.getenv("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = os.getenv("LLM_API_KEY", "")

# Get model configuration from environment
_provider = os.getenv("LLM_PROVIDER", "genai").lower().strip()
_model = os.getenv("LLM_MODEL", "gemini-2.5-flash-lite").strip()
_api_key = os.getenv("LLM_API_KEY", "").strip()

# Create a CrewAI LLM instance
_crew_llm = None


def _init_crew_llm():
    """Initialize CrewAI LLM wrapper."""
    global _crew_llm
    if _crew_llm is None:
        try:
            print(f"[DEBUG] Creating CrewAI LLM wrapper for model: {_model}", file=sys.stderr)
            # CrewAI's LLM class wraps the model and provider
            _crew_llm = LLM(
                model=_model,
                provider="google"  # Explicitly set provider to google for Gemini
            )
            print(f"[DEBUG] CrewAI LLM wrapper created successfully", file=sys.stderr)
        except Exception as e:
            print(f"[ERROR] Failed to create CrewAI LLM wrapper: {str(e)}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            raise ValueError(f"Cannot create CrewAI LLM: {str(e)}")
    return _crew_llm


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


def create_skills_agent():
    """Create the skills optimization agent."""
    try:
        llm = _init_crew_llm()
        agent = Agent(
            role="Resume Skills Section Specialist",
            goal="Craft a compelling, job-aligned skills section that accurately represents the candidate's technical and professional capabilities while maximizing relevance to target roles",
            backstory="You are a career strategist with 12+ years of experience optimizing resumes for tech professionals. You've helped hundreds of candidates land interviews at top companies by strategically positioning their skills. You understand how ATS systems work, what hiring managers look for, and how to present skills in a way that immediately demonstrates fit. You believe in authenticity - never inflating skills, but always presenting them in their best light.",
            system_prompt=SKILLS_AGENT_SYSTEM_PROMPT,
            allow_delegation=False,
            verbose=False,
            llm=llm,
        )
        print(f"[DEBUG] Skills agent created successfully", file=sys.stderr)
        return agent
    except Exception as e:
        print(f"[ERROR] Failed to create skills agent: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        raise ValueError(f"Failed to create skills agent: {str(e)}")


def create_education_agent():
    """Create the education optimization agent."""
    try:
        llm = _init_crew_llm()
        agent = Agent(
            role="Education & Credentials Strategist",
            goal="Transform the education section into a strategic asset that highlights relevant coursework, achievements, and certifications that directly support the candidate's target role",
            backstory="You are an academic advisor and career coach who specializes in helping professionals leverage their educational background for career advancement. With 10+ years of experience, you've learned how to identify and highlight the coursework, projects, and achievements that matter most to hiring managers. You're skilled at connecting academic experiences to professional outcomes and know how to present educational credentials in ways that strengthen a candidate's overall positioning.",
            system_prompt=EDUCATION_AGENT_SYSTEM_PROMPT,
            allow_delegation=False,
            verbose=False,
            llm=llm,
        )
        print(f"[DEBUG] Education agent created successfully", file=sys.stderr)
        return agent
    except Exception as e:
        print(f"[ERROR] Failed to create education agent: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        raise ValueError(f"Failed to create education agent: {str(e)}")


def create_experience_agent():
    """Create the experience optimization agent."""
    try:
        llm = _init_crew_llm()
        agent = Agent(
            role="Work Experience Impact Strategist",
            goal="Rewrite work experience bullets to powerfully demonstrate job-relevant accomplishments, technical skills, and measurable impact using language resonates with hiring managers",
            backstory="You're a veteran hiring manager who has reviewed thousands of resumes and conducted hundreds of interviews across technical roles. You know exactly what makes candidates stand out - it's not just what they did, but how they articulate the impact of their work. You've guided professionals at all levels to reframe their experiences in ways that highlight growth, leadership, and tangible outcomes. You understand that the best bullet points quantify impact and use precise, industry-standard terminology.",
            system_prompt=EXPERIENCE_AGENT_SYSTEM_PROMPT,
            allow_delegation=False,
            verbose=False,
            llm=llm,
        )
        print(f"[DEBUG] Experience agent created successfully", file=sys.stderr)
        return agent
    except Exception as e:
        print(f"[ERROR] Failed to create experience agent: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        raise ValueError(f"Failed to create experience agent: {str(e)}")


def create_projects_agent():
    """Create the projects optimization agent."""
    try:
        llm = _init_crew_llm()
        agent = Agent(
            role="Portfolio Projects Specialist",
            goal="Strategically reframe and prioritize projects to showcase job-relevant technical skills, architectural decisions, and measurable outcomes that demonstrate professional capability",
            backstory="You're a technical interviewer at leading tech companies who has evaluated hundreds of portfolios and conducted countless interviews. You've learned which projects impress and why. You understand that the best portfolio projects tell a story about the candidate's technical depth, problem-solving approach, and ability to ship real solutions. You're skilled at identifying the projects with the most impact and highlighting the technical decisions and learnings that matter most to target employers.",
            system_prompt=PROJECTS_AGENT_SYSTEM_PROMPT,
            allow_delegation=False,
            verbose=False,
            llm=llm,
        )
        print(f"[DEBUG] Projects agent created successfully", file=sys.stderr)
        return agent
    except Exception as e:
        print(f"[ERROR] Failed to create projects agent: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        raise ValueError(f"Failed to create projects agent: {str(e)}")


class ResumeOptimizationCrew:
    """Orchestrates the multi-agent resume optimization workflow."""

    def __init__(self, job_description: str, resume_context: dict):
        """
        Initialize the crew with job description and resume context.
        
        Args:
            job_description: The target job posting
            resume_context: Dictionary containing current resume sections and candidate info
        """
        self.job_description = job_description
        self.resume_context = resume_context

        # Create agents
        self.skills_agent = create_skills_agent()
        self.education_agent = create_education_agent()
        self.experience_agent = create_experience_agent()
        self.projects_agent = create_projects_agent()

    def optimize(self) -> dict:
        """
        Run the optimization crew and return optimized resume sections.
        
        Returns:
            Dictionary with optimized sections: skills, education, experience, projects
        """
        
        # Define tasks for each agent
        tasks = [
            Task(
                description=f"""Review the job description and the candidate's current skills section.
                
                Job Description:
                {self.job_description}

                Current Skills Section:
                {self.resume_context.get('skills', 'Not provided')}

                Candidate Background (for context):
                {self.resume_context.get('background', 'Not provided')}

                Optimize the skills section to match the job requirements while keeping only authentic skills.
                
                CRITICAL: Output ONLY the LaTeX section content (starting with \\vspace and \\section*{{Skills}}).
                Do NOT output full LaTeX documents with \\documentclass, \\usepackage, etc.""",
                agent=self.skills_agent,
                expected_output="ONLY LaTeX-formatted skills section content (5-6 lines starting with vspace and section*{Skills}). No document preamble.",
            ),
            Task(
                description=f"""Review the job description and the candidate's current education section.
                
                Job Description:
                {self.job_description}

                Current Education Section:
                {self.resume_context.get('education', 'Not provided')}

                Candidate Background:
                {self.resume_context.get('background', 'Not provided')}

                Optimize the education section to highlight relevant coursework and achievements.
                
                CRITICAL: Output ONLY the LaTeX section content (starting with \\vspace and \\section*{{Education}}).
                Do NOT output full LaTeX documents with \\documentclass, \\usepackage, etc.""",
                agent=self.education_agent,
                expected_output="ONLY LaTeX-formatted education section content (10-15 lines starting with vspace and section*{Education}). No document preamble.",
            ),
            Task(
                description=f"""Review the job description and the candidate's current experience section.
                
                Job Description:
                {self.job_description}

                Current Experience Section:
                {self.resume_context.get('experience', 'Not provided')}

                Candidate Background:
                {self.resume_context.get('background', 'Not provided')}

                Rewrite the experience bullets to align with job requirements while maintaining accuracy.
                
                CRITICAL: Output ONLY the LaTeX section content (starting with \\vspace and \\section*{{Work Experience}}).
                Do NOT output full LaTeX documents with \\documentclass, \\usepackage, etc.""",
                agent=self.experience_agent,
                expected_output="ONLY LaTeX-formatted work experience section content (15-25 lines starting with vspace and section*{Work Experience}). No document preamble.",
            ),
            Task(
                description=f"""Review the job description and the candidate's current projects section.
                
                Job Description:
                {self.job_description}

                Current Projects Section:
                {self.resume_context.get('projects', 'Not provided')}

                Candidate Background:
                {self.resume_context.get('background', 'Not provided')}

                Reframe and optimize the projects to highlight job-relevant technical skills.
                
                CRITICAL: Output ONLY the LaTeX section content (starting with \\vspace and \\section*{{Projects}}).
                Do NOT output full LaTeX documents with \\documentclass, \\usepackage, etc.""",
                agent=self.projects_agent,
                expected_output="ONLY LaTeX-formatted projects section content (10-20 lines starting with vspace and section*{Projects}). No document preamble.",
            ),
        ]

        # Create the crew
        crew = Crew(
            agents=[
                self.skills_agent,
                self.education_agent,
                self.experience_agent,
                self.projects_agent,
            ],
            tasks=tasks,
            verbose=False,
        )

        # Execute the crew
        result = crew.kickoff()

        # Parse the results from task outputs and clean the LaTeX
        optimized_sections = {
            "skills": _clean_latex_output(tasks[0].output.raw if tasks[0].output else ""),
            "education": _clean_latex_output(tasks[1].output.raw if tasks[1].output else ""),
            "experience": _clean_latex_output(tasks[2].output.raw if tasks[2].output else ""),
            "projects": _clean_latex_output(tasks[3].output.raw if tasks[3].output else ""),
        }

        return optimized_sections

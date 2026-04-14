"""
Resume optimization agents using CrewAI.
Each agent specializes in a specific resume section.
"""

from crewai import Agent, Task, Crew
from .config import (
    SKILLS_AGENT_SYSTEM_PROMPT,
    EDUCATION_AGENT_SYSTEM_PROMPT,
    EXPERIENCE_AGENT_SYSTEM_PROMPT,
    PROJECTS_AGENT_SYSTEM_PROMPT,
)


def create_skills_agent():
    """Create the skills optimization agent."""
    return Agent(
        role="Skills Optimizer",
        goal="Optimize the skills section to perfectly match job requirements while maintaining authenticity",
        backstory="You are a technical recruiter with 15+ years of experience. You know exactly what skills employers look for and how to present them effectively.",
        system_prompt=SKILLS_AGENT_SYSTEM_PROMPT,
        allow_delegation=False,
        verbose=False,
    )


def create_education_agent():
    """Create the education optimization agent."""
    return Agent(
        role="Education & Credentials Optimizer",
        goal="Enhance the education section to highlight relevant coursework and achievements aligned with the job",
        backstory="You are an academic advisor and career coach specializing in presenting educational qualifications to match job requirements.",
        system_prompt=EDUCATION_AGENT_SYSTEM_PROMPT,
        allow_delegation=False,
        verbose=False,
    )


def create_experience_agent():
    """Create the experience optimization agent."""
    return Agent(
        role="Experience & Achievements Optimizer",
        goal="Rewrite work experience bullets to highlight job-relevant skills and achievements",
        backstory="You are a senior hiring manager with experience across tech roles. You know exactly what bullet points catch attention and demonstrate the right fit.",
        system_prompt=EXPERIENCE_AGENT_SYSTEM_PROMPT,
        allow_delegation=False,
        verbose=False,
    )


def create_projects_agent():
    """Create the projects optimization agent."""
    return Agent(
        role="Projects Showcase Optimizer",
        goal="Reframe and prioritize projects to highlight job-relevant technical skills and achievements",
        backstory="You are a technical interviewer at leading tech companies. You understand what projects demonstrate the skills employers most value.",
        system_prompt=PROJECTS_AGENT_SYSTEM_PROMPT,
        allow_delegation=False,
        verbose=False,
    )


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

Optimize the skills section to match the job requirements while keeping only authentic skills.""",
                agent=self.skills_agent,
                expected_output="LaTeX formatted skills section with optimized skill categories and keywords",
            ),
            Task(
                description=f"""Review the job description and the candidate's current education section.
                
Job Description:
{self.job_description}

Current Education Section:
{self.resume_context.get('education', 'Not provided')}

Candidate Background:
{self.resume_context.get('background', 'Not provided')}

Optimize the education section to highlight relevant coursework and achievements.""",
                agent=self.education_agent,
                expected_output="LaTeX formatted education section with highlighted relevant coursework",
            ),
            Task(
                description=f"""Review the job description and the candidate's current experience section.
                
Job Description:
{self.job_description}

Current Experience Section:
{self.resume_context.get('experience', 'Not provided')}

Candidate Background:
{self.resume_context.get('background', 'Not provided')}

Rewrite the experience bullets to align with job requirements while maintaining accuracy.""",
                agent=self.experience_agent,
                expected_output="LaTeX formatted work experience section with optimized bullets",
            ),
            Task(
                description=f"""Review the job description and the candidate's current projects section.
                
Job Description:
{self.job_description}

Current Projects Section:
{self.resume_context.get('projects', 'Not provided')}

Candidate Background:
{self.resume_context.get('background', 'Not provided')}

Reframe and optimize the projects to highlight job-relevant technical skills.""",
                agent=self.projects_agent,
                expected_output="LaTeX formatted projects section with reframed descriptions",
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

        # Parse the results from task outputs
        optimized_sections = {
            "skills": tasks[0].output.raw if tasks[0].output else "",
            "education": tasks[1].output.raw if tasks[1].output else "",
            "experience": tasks[2].output.raw if tasks[2].output else "",
            "projects": tasks[3].output.raw if tasks[3].output else "",
        }

        return optimized_sections

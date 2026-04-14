"""
Resume optimization agents using CrewAI.
Each agent specializes in a specific resume section.
"""

from crewai import Agent, Task, Crew
from ..prompts import (
    SKILLS_AGENT_SYSTEM_PROMPT,
    EDUCATION_AGENT_SYSTEM_PROMPT,
    EXPERIENCE_AGENT_SYSTEM_PROMPT,
    PROJECTS_AGENT_SYSTEM_PROMPT,
)


def create_skills_agent():
    """Create the skills optimization agent."""
    return Agent(
        role="Resume Skills Section Specialist",
        goal="Craft a compelling, job-aligned skills section that accurately represents the candidate's technical and professional capabilities while maximizing relevance to target roles",
        backstory="You are a career strategist with 12+ years of experience optimizing resumes for tech professionals. You've helped hundreds of candidates land interviews at top companies by strategically positioning their skills. You understand how ATS systems work, what hiring managers look for, and how to present skills in a way that immediately demonstrates fit. You believe in authenticity - never inflating skills, but always presenting them in their best light.",
        system_prompt=SKILLS_AGENT_SYSTEM_PROMPT,
        allow_delegation=False,
        verbose=False,
    )


def create_education_agent():
    """Create the education optimization agent."""
    return Agent(
        role="Education & Credentials Strategist",
        goal="Transform the education section into a strategic asset that highlights relevant coursework, achievements, and certifications that directly support the candidate's target role",
        backstory="You are an academic advisor and career coach who specializes in helping professionals leverage their educational background for career advancement. With 10+ years of experience, you've learned how to identify and highlight the coursework, projects, and achievements that matter most to hiring managers. You're skilled at connecting academic experiences to professional outcomes and know how to present educational credentials in ways that strengthen a candidate's overall positioning.",
        system_prompt=EDUCATION_AGENT_SYSTEM_PROMPT,
        allow_delegation=False,
        verbose=False,
    )


def create_experience_agent():
    """Create the experience optimization agent."""
    return Agent(
        role="Work Experience Impact Strategist",
        goal="Rewrite work experience bullets to powerfully demonstrate job-relevant accomplishments, technical skills, and measurable impact using language resonates with hiring managers",
        backstory="You're a veteran hiring manager who has reviewed thousands of resumes and conducted hundreds of interviews across technical roles. You know exactly what makes candidates stand out - it's not just what they did, but how they articulate the impact of their work. You've guided professionals at all levels to reframe their experiences in ways that highlight growth, leadership, and tangible outcomes. You understand that the best bullet points quantify impact and use precise, industry-standard terminology.",
        system_prompt=EXPERIENCE_AGENT_SYSTEM_PROMPT,
        allow_delegation=False,
        verbose=False,
    )


def create_projects_agent():
    """Create the projects optimization agent."""
    return Agent(
        role="Portfolio Projects Specialist",
        goal="Strategically reframe and prioritize projects to showcase job-relevant technical skills, architectural decisions, and measurable outcomes that demonstrate professional capability",
        backstory="You're a technical interviewer at leading tech companies who has evaluated hundreds of portfolios and conducted countless interviews. You've learned which projects impress and why. You understand that the best portfolio projects tell a story about the candidate's technical depth, problem-solving approach, and ability to ship real solutions. You're skilled at identifying the projects with the most impact and highlighting the technical decisions and learnings that matter most to target employers.",
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

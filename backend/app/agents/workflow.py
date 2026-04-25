from .get_agent import AgentFactory
from langchain.tools import tool
from app.prompts import (
    SKILLS_AGENT_SYSTEM_PROMPT,
    EDUCATION_AGENT_SYSTEM_PROMPT,
    EXPERIENCE_AGENT_SYSTEM_PROMPT,
    PROJECTS_AGENT_SYSTEM_PROMPT,
)


# create the specialized agents for each resume section

# Skills Agent
skills_agents = AgentFactory(
    agent_name="SkillsAgent",
    system_prompt=SKILLS_AGENT_SYSTEM_PROMPT,
    tools=[], 
    ).create_agent()


# education agent
education_agent = AgentFactory(
    agent_name="EducationAgent", 
    system_prompt=EDUCATION_AGENT_SYSTEM_PROMPT, 
    tools=[], 
    ).create_agent()


# experience agent
experience_agent = AgentFactory(
    agent_name="ExperienceAgent",
    system_prompt=EXPERIENCE_AGENT_SYSTEM_PROMPT,
    tools=[],
    ).create_agent()


# projects agent
projects_agent = AgentFactory(
    agent_name="ProjectsAgent",
    system_prompt=PROJECTS_AGENT_SYSTEM_PROMPT,
    tools=[],
    ).create_agent()



# all agents in a dictionary for easy access
agents = {
    "skills_agent": skills_agents,
    "education_agent": education_agent,
    "experience_agent": experience_agent,
    "projects_agent": projects_agent,
}





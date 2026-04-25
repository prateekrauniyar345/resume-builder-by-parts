"""
Resume Optimization Workflow using LangGraph.
Implements supervisor-routed multi-agent pattern with judge node for feedback.
"""

from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from .get_agent import AgentFactory
from .get_llm import get_llm
from ..prompts import (
    SKILLS_AGENT_SYSTEM_PROMPT,
    EDUCATION_AGENT_SYSTEM_PROMPT,
    EXPERIENCE_AGENT_SYSTEM_PROMPT,
    PROJECTS_AGENT_SYSTEM_PROMPT,
)
import os


# ============================================================================
# STATE DEFINITION
# ============================================================================

class ResumeState(TypedDict):
    """State for resume optimization workflow."""
    messages: Annotated[list, add_messages]
    job_description: str
    resume_context: dict
    optimized_sections: dict
    judge_feedback: str


# ============================================================================
# AGENT CREATION
# ============================================================================

skills_agent = AgentFactory(
    agent_name="SkillsAgent",
    system_prompt=SKILLS_AGENT_SYSTEM_PROMPT,
    tools=[],
).create_agent()

education_agent = AgentFactory(
    agent_name="EducationAgent",
    system_prompt=EDUCATION_AGENT_SYSTEM_PROMPT,
    tools=[],
).create_agent()

experience_agent = AgentFactory(
    agent_name="ExperienceAgent",
    system_prompt=EXPERIENCE_AGENT_SYSTEM_PROMPT,
    tools=[],
).create_agent()

projects_agent = AgentFactory(
    agent_name="ProjectsAgent",
    system_prompt=PROJECTS_AGENT_SYSTEM_PROMPT,
    tools=[],
).create_agent()

agents = {
    "skills": skills_agent,
    "education": education_agent,
    "experience": experience_agent,
    "projects": projects_agent,
}


# ============================================================================
# NODE FUNCTIONS
# ============================================================================

def supervisor_node(state: ResumeState) -> ResumeState:
    """Supervisor node: initializes workflow and routes to worker agents."""
    return {
        "messages": [{"role": "assistant", "content": "Starting resume optimization..."}],
        "optimized_sections": {}
    }


def skills_node(state: ResumeState) -> ResumeState:
    """Skills optimization node."""
    prompt = f"""Optimize skills section for this job:

Job: {state['job_description']}
Current Skills: {state['resume_context'].get('skills', '')}
Context: {state['resume_context'].get('background', '')}

Return ONLY optimized LaTeX skills section."""
    
    result = skills_agent.invoke({"messages": [{"role": "user", "content": prompt}]})
    return {
        "messages": [{"role": "assistant", "content": "Skills optimized"}],
        "optimized_sections": {**state.get("optimized_sections", {}), "skills": str(result)}
    }


def education_node(state: ResumeState) -> ResumeState:
    """Education optimization node."""
    prompt = f"""Optimize education section for this job:

Job: {state['job_description']}
Current Education: {state['resume_context'].get('education', '')}
Context: {state['resume_context'].get('background', '')}

Return ONLY optimized LaTeX education section."""
    
    result = education_agent.invoke({"messages": [{"role": "user", "content": prompt}]})
    return {
        "messages": [{"role": "assistant", "content": "Education optimized"}],
        "optimized_sections": {**state.get("optimized_sections", {}), "education": str(result)}
    }


def experience_node(state: ResumeState) -> ResumeState:
    """Experience optimization node."""
    prompt = f"""Optimize experience section for this job:

Job: {state['job_description']}
Current Experience: {state['resume_context'].get('experience', '')}
Context: {state['resume_context'].get('background', '')}

Return ONLY optimized LaTeX experience section."""
    
    result = experience_agent.invoke({"messages": [{"role": "user", "content": prompt}]})
    return {
        "messages": [{"role": "assistant", "content": "Experience optimized"}],
        "optimized_sections": {**state.get("optimized_sections", {}), "experience": str(result)}
    }


def projects_node(state: ResumeState) -> ResumeState:
    """Projects optimization node."""
    prompt = f"""Optimize projects section for this job:

Job: {state['job_description']}
Current Projects: {state['resume_context'].get('projects', '')}
Context: {state['resume_context'].get('background', '')}

Return ONLY optimized LaTeX projects section."""
    
    result = projects_agent.invoke({"messages": [{"role": "user", "content": prompt}]})
    return {
        "messages": [{"role": "assistant", "content": "Projects optimized"}],
        "optimized_sections": {**state.get("optimized_sections", {}), "projects": str(result)}
    }


def judge_node(state: ResumeState) -> ResumeState:
    """Judge node: rates & provides feedback on optimized sections."""
    llm = get_llm()
    
    judge_prompt = f"""Review optimized resume for: {state['job_description'][:200]}

Optimized Sections:
- Skills: {state['optimized_sections'].get('skills', 'N/A')[:300]}
- Education: {state['optimized_sections'].get('education', 'N/A')[:300]}
- Experience: {state['optimized_sections'].get('experience', 'N/A')[:300]}
- Projects: {state['optimized_sections'].get('projects', 'N/A')[:300]}

Provide:
1. Quality Rating (1-10)
2. Strengths
3. Areas for improvement
4. Feedback per section"""
    
    feedback = llm.invoke(judge_prompt)
    feedback_text = getattr(feedback, 'content', str(feedback))
    
    return {
        "messages": [{"role": "assistant", "content": f"Judge Review:\n{feedback_text}"}],
        "judge_feedback": feedback_text
    }


# ============================================================================
# BUILD GRAPH
# ============================================================================

graph = StateGraph(ResumeState)

# Add nodes
graph.add_node("supervisor_node", supervisor_node)
graph.add_node("skills_node", skills_node)
graph.add_node("education_node", education_node)
graph.add_node("experience_node", experience_node)
graph.add_node("projects_node", projects_node)
graph.add_node("judge_node", judge_node)

# Edges
graph.add_edge(START, "supervisor_node")
graph.add_edge("supervisor_node", "skills_node")
graph.add_edge("supervisor_node", "education_node")
graph.add_edge("supervisor_node", "experience_node")
graph.add_edge("supervisor_node", "projects_node")
graph.add_edge("skills_node", "judge_node")
graph.add_edge("education_node", "judge_node")
graph.add_edge("experience_node", "judge_node")
graph.add_edge("projects_node", "judge_node")
graph.add_edge("judge_node", END)

# Compile
resume_workflow = graph.compile()


# ============================================================================
# SAVE GRAPH VISUALIZATION
# ============================================================================

def save_workflow_visualization():
    """Save workflow graph as PNG and Mermaid markdown files."""
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Save as Mermaid markdown
    mermaid_text = graph.get_graph().draw_mermaid()
    mermaid_path = os.path.join(output_dir, "workflow_graph.md")
    with open(mermaid_path, "w") as f:
        f.write("# Resume Optimization Workflow\n\n```mermaid\n")
        f.write(mermaid_text)
        f.write("\n```")
    
    # Save as PNG
    try:
        png_data = graph.get_graph().draw_mermaid_png()
        png_path = os.path.join(output_dir, "workflow_graph.png")
        with open(png_path, "wb") as f:
            f.write(png_data)
        print(f"Graph saved to {output_dir}/")
        print(f"   - workflow_graph.md (Mermaid text)")
        print(f"   - workflow_graph.png (PNG image)")
    except Exception as e:
        print(f"PNG export failed (graphviz may not be installed): {e}")
        print(f"   But Mermaid markdown saved to {mermaid_path}")

# Auto-save on import
try:
    save_workflow_visualization()
except Exception as e:
    print(f"Warning: Could not save workflow visualization: {e}")



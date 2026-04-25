"""
LangChain-based agent factory for resume optimization.
"""

from langchain.agents import create_agent
from langchain.tools import tool
from .get_llm import get_llm


class AgentFactory:
    """Factory for creating LangChain-based agents."""
    
    def __init__(self, agent_name, system_prompt, tools=None):
        """
        Initialize the agent factory.
        
        Args:
            agent_name: Name identifier for the agent
            system_prompt: System instruction prompt for the agent
            tools: List of Tool objects the agent can use (optional)
        """
        self.agent_name = agent_name
        self.system_prompt = system_prompt
        self.tools = tools or []
    
    def create_agent(self):
        """
        Create and return a LangChain agent.
        
        Returns:
            A configured LangChain agent executor
        """
        llm = get_llm()
        
        # Create the agent with ReAct framework
        agent = create_agent(
            llm=llm,
            tools=self.tools,
            prompt=self.system_prompt,
        )
        
        return agent


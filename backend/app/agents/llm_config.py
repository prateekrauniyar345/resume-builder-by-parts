"""
LLM configuration for resume optimization agents.
Supports multiple providers: Cerebras, OpenAI, Anthropic.
Provider, model, and API key are configured via environment variables.
"""

import os
from langchain_cerebras import ChatCerebras
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


def get_llm():
    """
    Get an LLM instance based on environment variables.
    
    Environment variables required:
        - LLM_PROVIDER: 'cerebras', 'openai', or 'anthropic'
        - LLM_MODEL: Model name for the selected provider
        - CEREBRAS_API_KEY, OPENAI_API_KEY, or ANTHROPIC_API_KEY: API key for the provider
        
    Returns:
        LLM instance configured for the specified provider
    """
    # Get configuration from environment variables
    provider = os.getenv("LLM_PROVIDER", "cerebras").lower()
    model = os.getenv("LLM_MODEL")
    
    if provider == "cerebras":
        api_key = os.getenv("CEREBRAS_API_KEY")
        if not api_key:
            raise ValueError(
                "CEREBRAS_API_KEY environment variable not set. "
                "Please set it before using Cerebras as LLM provider."
            )
        
        if not model:
            model = "llama-3.1-70b"
        
        return ChatCerebras(
            api_key=api_key,
            model=model,
            temperature=0.7,
            max_tokens=2048,
        )
    
    elif provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        if not model:
            model = "gpt-4-turbo"
        
        return ChatOpenAI(
            api_key=api_key,
            model=model,
            temperature=0.7,
        )
    
    elif provider == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        
        if not model:
            model = "claude-3-opus-20240229"
        
        return ChatAnthropic(
            api_key=api_key,
            model=model,
            temperature=0.7,
        )
    
    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}. "
            "Supported providers: cerebras, openai, anthropic"
        )


# Get default LLM instance
try:
    DEFAULT_LLM = get_llm()
except ValueError as e:
    print(f"Warning: Could not initialize default LLM: {e}")
    DEFAULT_LLM = None

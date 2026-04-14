import os
from langchain_cerebras import ChatCerebras
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from google import genai
from dotenv import load_dotenv

load_dotenv()


def get_llm():
    provider = os.getenv("LLM_PROVIDER", "").lower()
    model = os.getenv("LLM_MODEL", "")

    if provider == "cerebras":
        api_key = os.getenv("CEREBRAS_API_KEY")
        if not api_key:
            raise ValueError("CEREBRAS_API_KEY environment variable not set")
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

    elif provider == "genai":
        api_key = os.getenv("LLM_API_KEY")
        if not api_key:
            raise ValueError("LLM_API_KEY environment variable not set for GenAI provider")
        if not model:
            model = "gemini-3.1-flash-lite-preview"
        return genai.Client(api_key=api_key)

    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}. "
            "Supported providers: cerebras, openai, anthropic, genai"
        )
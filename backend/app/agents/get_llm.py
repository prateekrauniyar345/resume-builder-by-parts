# this file provides a llm that can be used in anyway we want

from langchain_openai import ChatOpenAI
import os


def get_llm():
    model = os.getenv("LLM_MODEL", "gpt-5-mini").strip().lower()
    api_key = os.getenv("LLM_API_KEY", "").strip()
    return ChatOpenAI(
        model=model,
        api_key=api_key,
        max_retries=2,
        temperature=0.7,
        reasoning_effort="medium",
    )
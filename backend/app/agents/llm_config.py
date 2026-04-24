import os
import sys
from dotenv import load_dotenv
from langchain_cerebras import ChatCerebras
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_llm():
    """Get configured LLM instance based on environment variables.
    
    Returns:
        BaseLLM: A LangChain BaseLLM instance configured with the specified provider.
        
    Raises:
        ValueError: If provider is unsupported or required API key is missing.
    """
    provider = os.getenv("LLM_PROVIDER", "").lower().strip()
    model = os.getenv("LLM_MODEL", "").strip()
    
    # Log configuration for debugging
    print(f"[DEBUG] Initializing LLM: provider={provider}, model={model}", file=sys.stderr)

    if provider == "cerebras":
        api_key = os.getenv("CEREBRAS_API_KEY")
        if not api_key:
            raise ValueError("CEREBRAS_API_KEY environment variable not set")
        if not model:
            model = "llama-3.1-70b"
        print(f"[DEBUG] Initializing Cerebras LLM with model={model}", file=sys.stderr)
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
        print(f"[DEBUG] Initializing OpenAI LLM with model={model}", file=sys.stderr)
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
        print(f"[DEBUG] Initializing Anthropic LLM with model={model}", file=sys.stderr)
        return ChatAnthropic(
            api_key=api_key,
            model=model,
            temperature=0.7,
        )

    elif provider == "genai" or provider == "google" or provider == "":
        api_key = os.getenv("LLM_API_KEY")
        if not api_key:
            raise ValueError("LLM_API_KEY environment variable not set for Gemini provider")
        if not model:
            model = "gemini-2.5-flash-lite"
        
        print(f"[DEBUG] Initializing ChatGoogleGenerativeAI with model={model}", file=sys.stderr)
        
        # Initialize ChatGoogleGenerativeAI with proper parameters
        try:
            llm = ChatGoogleGenerativeAI(
                model=model,
                google_api_key=api_key,
                temperature=0.7,
                convert_system_message_to_human=True,
            )
            print(f"[DEBUG] ChatGoogleGenerativeAI created: {type(llm)}", file=sys.stderr)
            print(f"[DEBUG] LLM model_name: {llm.model_name if hasattr(llm, 'model_name') else 'N/A'}", file=sys.stderr)
            return llm
        except Exception as e:
            print(f"[ERROR] Failed to initialize ChatGoogleGenerativeAI: {str(e)}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            raise ValueError(f"Failed to initialize Gemini LLM: {str(e)}")

    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}. "
            "Supported providers: cerebras, openai, anthropic, genai, google"
        )
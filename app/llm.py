from app.config import LLM_PROVIDER
from app.exceptions import LLMError

def call_llm(prompt: str) -> str:
    if LLM_PROVIDER == "local":
        return local_llm(prompt)
    elif LLM_PROVIDER == "openai":
        raise LLMError("OpenAI integration not enabled")
    elif LLM_PROVIDER == "bedrock":
        raise LLMError("Bedrock integration not enabled")
    else:
        raise LLMError("Invalid LLM_PROVIDER")

def local_llm(prompt: str) -> str:
    return prompt.split("Context:")[-1].split(".")[0].strip()

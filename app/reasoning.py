from app.llm import call_llm
from app.exceptions import ReasoningError

def reason(context: str, question: str) -> str:
    try:
        if not context.strip():
            return "I don't know"

        prompt = f"""
                You are a factual assistant.

                Context:
                {context}

                Question:
                {question}
                """
        answer = call_llm(prompt)
        return answer if answer else "I don't know"

    except Exception as e:
        raise ReasoningError(str(e))

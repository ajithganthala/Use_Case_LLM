from app.retrieval import retrieve_documents
from app.history import get_history, save_turn
from app.reasoning import reason

def answer_question(question: str, session_id: str) -> str:
    docs = retrieve_documents(question)

    if not docs:
        return "I don't know"

    history = get_history(session_id)
    context = "\n".join([d["text"] for d in docs] + history)

    answer = reason(context, question)
    save_turn(session_id, question, answer)

    return answer

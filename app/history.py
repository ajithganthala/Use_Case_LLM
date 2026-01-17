from collections import defaultdict
from app.config import MAX_HISTORY_TURNS

_HISTORY = defaultdict(list)

def get_history(session_id: str):
    return _HISTORY[session_id][-MAX_HISTORY_TURNS:]

def save_turn(session_id: str, q: str, a: str):
    _HISTORY[session_id].append(f"Q:{q} A:{a}")

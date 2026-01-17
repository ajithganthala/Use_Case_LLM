from pydantic import BaseModel, Field
from typing import Dict, Any

class DocumentIn(BaseModel):
    id: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)
    metadata: Dict[str, Any]

class QuestionIn(BaseModel):
    question: str = Field(..., min_length=3)
    session_id: str = Field(..., min_length=1)

class AnswerOut(BaseModel):
    answer: str

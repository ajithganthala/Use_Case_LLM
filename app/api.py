import time
from fastapi import APIRouter, HTTPException, Query
from elasticsearch import Elasticsearch

from app.config import ES_INDEX
from app.models import DocumentIn, QuestionIn, AnswerOut
from app.embeddings import embed_text
from app.retrieval import retrieve_documents
from app.rag import answer_question
from app.evaluation import log_eval

router = APIRouter()
es = Elasticsearch("http://localhost:9200")

@router.post("/documents")
def ingest_document(doc: DocumentIn):
    try:
        embedding = embed_text(doc.text)

        es.index(
            index=ES_INDEX,
            id=doc.id,
            document={
                "text": doc.text,
                "metadata": doc.metadata,
                "embedding": embedding,
            }
        )

        return {"status": "success", "document_id": doc.id}

    except Exception as e:
        raise HTTPException(500, f"Document ingestion failed: {e}")

@router.get("/search")
def search(q: str = Query(..., min_length=2)):
    try:
        return {"results": retrieve_documents(q)}
    except Exception as e:
        raise HTTPException(503, str(e))

@router.post("/qa", response_model=AnswerOut)
def qa(payload: QuestionIn):
    start = time.time()
    try:
        answer = answer_question(payload.question, payload.session_id)
        log_eval(time.time() - start, answer)
        return AnswerOut(answer=answer)
    except Exception as e:
        raise HTTPException(500, str(e))

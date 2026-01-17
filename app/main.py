from fastapi import FastAPI
from app.api import router
from app.logging_config import setup_logging

setup_logging()

app = FastAPI(title="Production RAG QA Service")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}

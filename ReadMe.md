# AI Document QA Service (Production-Grade RAG)

This repository contains a **production-oriented AI Document Question Answering (QA) service** built using **FastAPI, Elasticsearch, and Retrieval-Augmented Generation (RAG)**.

The system is designed to demonstrate **real-world engineering practices**, including:

* Hybrid retrieval (BM25 + vector embeddings)
* Conversational history management
* Deterministic reasoning with LLM abstraction
* Robust error handling
* Observability and evaluation hooks
* Clean, modular architecture

---

## Project Structure - Folder

Main_Folder
  app
    api.py
    cofig.py
    embeddings.py
    evaluation.py
    exceptions.py
    history.py
    llm.py
    logging_config.py
    main.py
    models.py
    rag.py
    reasoning.py
    retrieval.py
  tests
    test_api.py
    test_reasoning.py
    test_retrieval.oy
  requirements.txt
  readme.md

## Core Application Files (`app/`)

### `main.py`

**Application entry point**

* Initializes logging
* Creates the FastAPI application
* Registers API routes
* Exposes health-check endpoint

This file wires together all components and starts the service.

---

### `config.py`

**Centralized configuration**

Defines runtime configuration such as:

* Elasticsearch host and index
* Retrieval parameters (Top-K)
* History limits
* Embedding dimensions
* LLM provider flag (`local`, `openai`, `bedrock`)

Keeps configuration separate from business logic.

---

### `logging_config.py`

**Logging bootstrap**

* Configures structured application logging
* Ensures logs are written to stdout (container-friendly)
* Used once during application startup

Supports observability and production debugging.

---

### `exceptions.py`

**Domain-specific exception definitions**

Defines custom exceptions such as:

* `SearchServiceUnavailable`
* `EmbeddingError`
* `ReasoningError`
* `LLMError`

Enables clean separation between:

* Business logic errors
* Infrastructure failures
* API-level error handling

---

### `models.py`

**API request/response schemas**

Uses Pydantic models for:

* Document ingestion (`DocumentIn`)
* QA requests (`QuestionIn`)
* QA responses (`AnswerOut`)

Provides:

* Input validation
* Type safety
* Automatic 422 responses for invalid payloads

---

### `embeddings.py`

**Text embedding generation**

* Generates deterministic vector embeddings for text
* Used during document ingestion and query-time retrieval
* Implemented locally to avoid external dependencies

This module can be easily swapped with:

* Sentence Transformers
* OpenAI embeddings
* Bedrock embeddings

---

### `retrieval.py`

**Hybrid document retrieval**

* Performs Elasticsearch-based hybrid search:

  * Keyword matching (BM25)
  * Vector similarity (cosine similarity)
* Returns top-K relevant documents
* Handles Elasticsearch failures gracefully

This is the **core retrieval layer** of the RAG pipeline.

---

### `history.py`

**Conversation history management**

* Stores conversation turns per session
* Enforces last-N history limit
* Prevents unbounded context growth

History is treated as:

* Auxiliary context
* Never a source of truth
* Fully discardable if unavailable

---

### `llm.py`

**LLM abstraction layer**

* Selects LLM provider via feature flag
* Supports:

  * Local deterministic reasoning
  * OpenAI (placeholder)
  * Bedrock (placeholder)

This abstraction allows **LLM swapping without code changes**.

---

### `reasoning.py`

**Answer generation logic**

* Constructs the final prompt
* Calls the LLM abstraction
* Enforces hallucination-safe behavior
* Returns `"I don't know"` when context is insufficient

Ensures answers are:

* Grounded
* Deterministic
* Auditable

---

### `rag.py`

**RAG orchestration layer**

Coordinates the full RAG flow:

1. Document retrieval
2. History fetch
3. Context construction (Docs > History)
4. Reasoning
5. History persistence

This file represents the **core intelligence pipeline**.

---

### `evaluation.py`

**Evaluation & observability hooks**

* Logs latency and answer characteristics
* Designed to integrate with:

  * Offline benchmarks
  * Online dashboards
  * Alerting systems

Supports evaluation-driven development.

---

### `api.py`

**REST API endpoints**

Implements all required endpoints:

#### `POST /documents`

* Ingests documents
* Generates embeddings
* Indexes content into Elasticsearch

#### `GET /search`

* Performs hybrid document search
* Returns top-K results

#### `POST /qa`

* Executes full RAG pipeline
* Supports conversational sessions
* Logs evaluation metrics

This file translates **business logic into HTTP APIs**.

---

## Tests (`tests/`)

### `test_reasoning.py`

* Validates deterministic reasoning behavior
* Ensures safe fallback when context is empty

### `test_retrieval.py`

* Retrieval layer smoke tests
* Ensures search pipeline stability

### `test_api.py`

* API availability smoke tests
* Validates endpoint wiring

These tests provide a foundation for CI/CD expansion.

---

## Running the Service

### Start Elasticsearch

```bash
docker run -p 9200:9200 -e "discovery.type=single-node" elasticsearch:8.11.1
```

### Start API

```bash
uvicorn app.main:app --reload
```

### Run Tests

```bash
pytest
```

---

## Design Principles Demonstrated

* Retrieval-Augmented Generation (RAG)
* Hybrid search (keyword + vector)
* Conversational memory with safeguards
* Fail-soft system design
* LLM vendor abstraction
* Production-ready observability
* Clear separation of concerns

---

## Final Note

This project intentionally prioritizes **clarity, correctness, and robustness** over feature volume.
It mirrors how **real production AI systems** are designed, operated, and evaluated.

---

**End of README**

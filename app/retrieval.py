import logging
from elasticsearch import Elasticsearch
from app.config import ES_HOST, ES_INDEX, TOP_K
from app.embeddings import embed_text
from app.exceptions import SearchServiceUnavailable

logger = logging.getLogger(__name__)
es = Elasticsearch(ES_HOST)

def retrieve_documents(query: str):
    try:
        query_vector = embed_text(query)

        response = es.search(
            index=ES_INDEX,
            size=TOP_K,
            query={
                "script_score": {
                    "query": {"match": {"text": query}},
                    "script": {
                        "source": "cosineSimilarity(params.q, 'embedding') + 1.0",
                        "params": {"q": query_vector},
                    },
                }
            },
        )

        return [
            {
                "id": hit["_id"],
                "text": hit["_source"]["text"],
                "score": hit["_score"],
            }
            for hit in response["hits"]["hits"]
        ]

    except Exception as e:
        logger.exception("Hybrid retrieval failed")
        raise SearchServiceUnavailable(str(e))

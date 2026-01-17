##These are local Embeddings

import numpy as np
from app.exceptions import EmbeddingError

def embed_text(text: str) -> list[float]:
    try:
        np.random.seed(abs(hash(text)) % (10**6))
        return np.random.rand(384).tolist()
    except Exception as e:
        raise EmbeddingError(str(e))

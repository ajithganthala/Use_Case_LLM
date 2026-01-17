class AppError(Exception):
    pass

class SearchServiceUnavailable(AppError):
    pass

class EmbeddingError(AppError):
    pass

class ReasoningError(AppError):
    pass

class LLMError(AppError):
    pass

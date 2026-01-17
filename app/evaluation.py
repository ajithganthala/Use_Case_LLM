import logging
logger = logging.getLogger(__name__)

def log_eval(latency: float, answer: str):
    logger.info("EVAL | latency=%.3f | answer_len=%d", latency, len(answer))

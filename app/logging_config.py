import logging
import sys
from app.config import LOG_LEVEL

def setup_logging():
    try:
        logging.basicConfig(level=LOG_LEVEL,format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",handlers=[logging.StreamHandler(sys.stdout)])
    except:
        raise Exception

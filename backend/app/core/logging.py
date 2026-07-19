import logging
from .config import settings

def setup_logging():
    logging.basicConfig(level=settings.LOG_LEVEL)
    return logging.getLogger("stadiumops")

logger = setup_logging()

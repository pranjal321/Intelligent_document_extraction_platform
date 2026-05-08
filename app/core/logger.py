from functools import wraps
from loguru import logger

logger.add(
    "logs/app.log",
    rotation="10 MB"
)


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        logger.info(f"Running: {func.__name__}")

        result = func(*args, **kwargs)

        logger.info(f"Completed: {func.__name__}")

        return result

    return wrapper
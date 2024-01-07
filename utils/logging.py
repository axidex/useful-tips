import functools
import logging

from typing import Any, Callable

def with_logging_dec(logger: logging.Logger):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.info(f"Calling {func.__name__}")
            value = func(*args, **kwargs)
            logger.info(f"Finished {func.__name__}")
            return value

        return wrapper

    return decorator

def with_logging(
    func: Callable[..., Any], logger: logging.Logger
) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.info(f"Calling {func.__name__}")
        value = func(*args, **kwargs)
        logger.info(f"Finished {func.__name__}")
        return value

    return wrapper

def get_logger_decorator(logger):
    return functools.partial(with_logging, logger=logger)
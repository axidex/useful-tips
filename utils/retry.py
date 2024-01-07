import time
from functools import wraps


def retry(max_retries=4, timeout=1, retry_exc_class=Exception, raise_exc_class=Exception):
    def retry_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    print(f"decorator: {args}")
                    return func(*args, **kwargs)
                except retry_exc_class as ex:
                    print(f"Error was found in {func.__name__} | {ex}")
                    print(f"retries left {max_retries-i-1}")
                    time.sleep(timeout)

            raise raise_exc_class(f"Cannot run func {func.__name__} after {max_retries} tries") from retry_exc_class

        return wrapper
    return retry_decorator

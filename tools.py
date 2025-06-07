from time import perf_counter
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        stop = perf_counter()
        print(f'{func.__name__}: {(stop - start):.10f}s')
        return result
    return wrapper
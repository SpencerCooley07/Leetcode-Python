from time import perf_counter
from functools import wraps

def timer(n=10):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(n):
                start = perf_counter()
                func(*args, **kwargs)
                stop = perf_counter()
                total_time += (stop - start)
            print(f'{func.__name__} average over {n} runs: {(total_time/n):.10f}s\nResult: {func(*args, **kwargs)}')
        return wrapper
    return decorator
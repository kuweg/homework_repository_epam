def print_debugger(func):
    """Small decorator for debugging purposes."""

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"{func.__name__} : {res}")
        return res

    return wrapper

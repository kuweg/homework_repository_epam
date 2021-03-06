"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""

from typing import Callable


def cache(func: Callable) -> Callable:
    """
    Implementation of cache function, which stores
    result of function (func).
    """
    function_excution_results_dict = {}

    def wrapper(*args):
        if args not in function_excution_results_dict:
            function_excution_results_dict[args] = func(*args)
        return function_excution_results_dict[args]
    return wrapper

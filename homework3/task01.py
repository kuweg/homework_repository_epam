"""
In previous homework task 4, you wrote a cache function
that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        # careful with input() in python2, use raw_input() instead
        return input('? ')

    >>> f()
    ? 1
    '1'
    >>> f() # will remember previous value
    '1'
    >>> f() # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""

from typing import Callable


def cache(times: int) -> Callable:
    """
    Implementation of cache function, which stores
    result of function (func) only 'times'.
    """
    if not isinstance(times, int) or times <= 0:
        raise AttributeError("Expected times argument to be integer and > 0")
    function_execution_results_dict = {}

    def outer(func: Callable) -> Callable:
        def wrapper(*args):

            if (
                args not in function_execution_results_dict
                or not function_execution_results_dict[args][1]
            ):
                function_execution_results_dict[args] = [func(*args), times]

            function_execution_results_dict[args][1] -= 1
            return function_execution_results_dict[args]

        return wrapper

    return outer


@cache(times=2)
def foo(a, b):
    return a * b


a = foo(2, 3)
b = foo(2, 3)
c = foo(2, 3)
assert b is not c

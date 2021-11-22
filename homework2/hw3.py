"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from itertools import product
from typing import Any, List


def make_combinations(*args: List[Any]) -> List[List]:
    """
    Producing all posiible combinations of lists
    using itertools.
    itertools docs:
    https://docs.python.org/3/library/itertools.html#itertools.product
    """
    combinations_tuples_in_list = list(product(*args))
    combinations_list = [
        list(combination) for combination in combinations_tuples_in_list
        ]
    return combinations_list

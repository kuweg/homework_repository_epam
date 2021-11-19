"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(
    string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(
    string.ascii_lowercase, 'g', 'p'
    ) == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(
    string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, List


def custom_range(input_sequence: List[Any], *args) -> List[Any]:
    """
    Implementing a custom range function
    which allows to iterate through any iterable object
    with unique values.
    """
    range_args = []
    if len(args) > 3:
        args = args[:3]
    for num, arg in enumerate(args):
        if num < 2:
            arg = input_sequence.index(arg)
        range_args.append(arg)
    range_args = tuple(range_args)
    custom_range_result = [
        input_sequence[element] for element in range(*range_args)
        ]
    return custom_range_result

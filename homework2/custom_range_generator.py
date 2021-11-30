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
from typing import Any, Generator, Iterable, List


def prepare_slice_args_for_sequence(
        sequence: Iterable[any], *args
        ) -> List[any]:
    """
    Preparing input arguments for custom range generator.
    """
    slice_args = []
    _max_args = 3
    _position_args = 2

    for num, arg in enumerate(args[:_max_args]):
        if num < _position_args:
            arg = sequence.index(arg)
        slice_args.append(arg)
    range_args = tuple(slice_args)
    return range_args


def custom_range_generator(input_sequence: List[Any], *args) -> Generator:
    """Implementing a generator, which returns values
    from a specific user-based range.
    """
    slice_args = prepare_slice_args_for_sequence(input_sequence, *args)
    len_args = len(slice_args)
    if len_args == 1:
        for element in input_sequence[: slice_args[0]]:
            yield element

    elif len_args == 2:
        for element in input_sequence[slice_args[0]: slice_args[1]]:
            yield element

    elif len_args == 3:
        for element in input_sequence[
                slice_args[0]: slice_args[1]: slice_args[2]
                ]:
            yield element


def make_custom_range(
        input_sequence: Iterable[any], *args, **kwargs
        ) -> List[any]:
    """
    Implementing a custom range function
    which can accumulate generator's output.
    Supports a mode kwargs: ('list', 'generator').
    """
    mode = ""
    keys = list(kwargs.keys())
    if "mode" in keys:
        mode = kwargs["mode"]

    custom_range = custom_range_generator(input_sequence, *args)
    if mode == "generator":
        return custom_range
    return list(custom_range)

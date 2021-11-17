"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""

from functools import cache
from math import sqrt
from typing import Sequence


@cache
def check__if_prefect_square(number):
    """
    checking if the number can be from the fibonacci sequence.
    Source:
    https://en.wikipedia.org/wiki/Fibonacci_number#Identification"""

    if (sqrt(5 * (number ** 2) - 4) % 1 == 0 or
            sqrt(5 * (number ** 2) + 4) % 1 == 0):
        return True


def check_fibonacci(inp_sequence: Sequence[int]) -> bool:
    """Cheking sequence for being a fibonacci sequence."""

    # Checking does a sequince is empty to avoid
    # unnecessary calculations
    if not len(inp_sequence):
        return False

    # Checking did a first two numbers a fibonacci numbers
    # using a perfect square
    first_elem = inp_sequence[0]
    if len(inp_sequence) == 1:
        if first_elem == 0:
            return True
        elif first_elem != 0:
            if not check__if_prefect_square(first_elem):
                return False
    else:
        second_elem = inp_sequence[1]
        if first_elem != 0:
            if not check__if_prefect_square(first_elem):
                return False
        if second_elem != 0:
            if not check__if_prefect_square(second_elem):
                return False
    # Checking does the rest part of sequence is valid
    for i in range(2, len(inp_sequence)):
        if inp_sequence[i] != inp_sequence[i-1] + inp_sequence[i-2]:
            return False
    return True

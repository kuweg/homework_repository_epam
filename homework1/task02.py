"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""

from math import sqrt
from typing import Sequence

"implementation of perfect square formula"


def check_prefect_square(elem):
    if (sqrt(5 * (elem ** 2) - 4) % 1 == 0 or
            sqrt(5 * (elem ** 2) + 4) % 1 == 0):
        return True


def check_fibonacci(data: Sequence[int]) -> bool:
    "Cheking sequence for being a fibonacci sequence"

    "If data is empty return False"
    if not len(data):
        return False
    """
    Checking did a first two numbers a fibonacci numbers
    using a perfect square:
    https://en.wikipedia.org/wiki/Fibonacci_number#Identification
     """
    if len(data) == 1:
        if data[0] == 0:
            return True
        elif data[0] != 0:
            if not check_prefect_square(data[0]):
                return False
    else:
        if data[0] != 0:
            if not check_prefect_square(data[0]):
                return False
        if data[1] != 0:
            if not check_prefect_square(data[1]):
                return False
    "Checking does the rest part of sequence is valid"
    for i in range(2, len(data)):
        if data[i] != data[i-1] + data[i-2]:
            return False
    return True

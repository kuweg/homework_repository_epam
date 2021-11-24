"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Return list with fizzbuzz numbers.
    For doctest run 'pytest --doctest-modules'

    >>> fizzbuzz(3)
    ['1', '2', 'fizz']

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',
    'buzz', '11', 'fizz', '13', '14', 'fizz buzz']
    """
    fizzbuzz_sequence = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            fizzbuzz_sequence.append("fizz buzz")
        elif number % 3 == 0:
            fizzbuzz_sequence.append("fizz")
        elif number % 5 == 0:
            fizzbuzz_sequence.append("buzz")
        else:
            fizzbuzz_sequence.append(str(number))
    return fizzbuzz_sequence

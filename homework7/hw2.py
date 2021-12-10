"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from typing import Generator


def backspace_formatter(string: str, backspace_char: str = "#") -> Generator:
    """A functions which imitates a backspace behaviour."""
    backspace_counter = 0
    for char in reversed(string):
        if char != backspace_char and not backspace_counter:
            yield char
        elif char == backspace_char:
            backspace_counter += 1
        elif char != backspace_char and backspace_counter > 0:
            backspace_counter -= 1


def backspace_compare(first: str, second: str) -> bool:
    """Picking items from generators and compare them."""
    first_string = backspace_formatter(first)
    second_string = backspace_formatter(second)
    try:
        while True:
            if next(first_string) != next(second_string):
                return False
    except StopIteration:
        return True


if __name__ == "__main__":
    string1 = "ab#c"
    string2 = "ad#c"
    c = backspace_compare(string1, string2)
    print(c)

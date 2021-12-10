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


def backspace_formatter(string: str, backspace_char: str = "#") -> str:
    """A functions which imitates a backspace behaviour."""
    formatted_list = []
    for char in string:
        if char != backspace_char:
            formatted_list.append(char)
        elif formatted_list:
            formatted_list.pop()
    formatted_string = "".join(formatted_list)
    return formatted_string


def backspace_compare_slow(first: str, second: str):
    return backspace_formatter(first) == backspace_formatter(second)


if __name__ == "__main__":
    string1 = "ab#c"
    string2 = "ad#c"
    print(backspace_compare_slow(string1, string2))

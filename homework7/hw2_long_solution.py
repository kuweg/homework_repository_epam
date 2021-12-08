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
from typing import Any, List


def print_debugger(func):
    """Small decorator for debugging purposes."""
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{func.__name__} : {res}')
        return res
    return wrapper


def flatten(list_of_lists: List[List]) -> List[Any]:
    """Helper function which flatten a two-dimensional list."""
    return [item for sublist in list_of_lists
            for item in sublist]


# @print_debugger
def find_backspace_indexes(
    target_string: str, target_character: str
        ) -> List[Any]:
    """Function which finds all indexes of target character in given str."""
    pos_list = [
        pos for pos, char in enumerate(target_string)
        if char == target_character
            ]
    return pos_list


# @print_debugger
def find_backspace_intervals(target_list: List[int]) -> List[List]:
    """
    A helper function which groups a backspaces positions
    into intervals.
    Example: [1, 3, 4, 6] -> [[1], [3, 4], [6]]
    """
    if not target_list:
        return []

    last_index = 0
    indexes_list = []
    buffer = [target_list[0]]
    target_list_len = len(target_list)
    for index in range(target_list_len - 1):
        if target_list[index+1] - target_list[index] == 1:
            buffer.append(target_list[index+1])
        else:
            indexes_list.append(buffer)
            last_index = index + 1
            buffer = [target_list[last_index]]

    indexes_list.append(buffer)
    return indexes_list


# @print_debugger
def process_intervals(intervals: List[List]) -> List[List]:
    """
    A helper function to add a left boundary to interval
    and fill missing indexes.
    Example: [[1], [3, 4], [6]] -> [[0,1], [1, 2, 3 ,4], [5, 6]]
    """
    new_intervals = []
    for interval in intervals:
        left_boundary = interval[0] - len(interval)
        right_boundary = interval[-1] + 1
        if left_boundary < 0:
            new_intervals.append(list(range(0, right_boundary)))
        else:
            new_intervals.append(list(range(left_boundary, right_boundary)))
    return new_intervals


# @print_debugger
def find_indexes_to_remove(target_sequence: str, target_character: str):
    """Returns list of indexes to delete."""
    backspace_positions = find_backspace_indexes(
        target_sequence, target_character
            )
    backspace_intervals = find_backspace_intervals(backspace_positions)
    backspace_indexes = process_intervals(backspace_intervals)
    return flatten(backspace_indexes)


# @print_debugger
def backspace_formatter(target_string: str, backspace_char: str) -> str:
    """Returns formatted string."""
    formatted_list = []
    removal_indexes = find_indexes_to_remove(target_string, backspace_char)
    formatted_list = [char for pos, char in enumerate(target_string)
                      if pos not in removal_indexes]
    formatted_string = ''.join(formatted_list)
    return formatted_string


# @print_debugger
def backspace_compare(first: str, second: str) -> bool:
    backspace_symbol = '#'
    first_string = backspace_formatter(first, backspace_symbol)
    second_string = backspace_formatter(second, backspace_symbol)
    return first_string == second_string


if __name__ == '__main__':

    a1 = 'ad#c'
    a2 = 'ab#c'
    print(backspace_compare(a1, a2))

"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def print_debugger(func):
    """Small decorator for debugging purposes."""
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"{func.__name__} : {res}")
        return res

    return wrapper


# @print_debugger
def check_types(child_value: Any, desired_type: type) -> bool:
    """Checks does a list contains a element with desired type."""
    if type(child_value) not in [int, bool]:
        types_list = [type(item) for item in child_value]
        return desired_type in types_list
    return desired_type is child_value


# @print_debugger
def find_elements_indexes_by_type(
    elements_list: list, desired_type: type
        ) -> list:
    """A helper function which returns
    all occurrences of element with desired type."""
    elements_indexes = []
    if any(isinstance(element, desired_type) for element in elements_list):
        for index, element in enumerate(elements_list):
            if isinstance(element, desired_type):
                elements_indexes.append(index)
        return elements_indexes
    return False


# @print_debugger
def contains(value: Any, item: Any) -> bool:
    """A little bit hardcoded function to compare two elements."""
    if type(value) is dict:
        return False

    if type(value) is str and type(item) is str:
        return value == item
    elif type(value) is int and type(item) is int:
        return value == item
    elif type(value) is bool and type(item) is bool:
        return value is item
    elif ((type(value) is list) or (type(value) is tuple)) and (
        type(item) in [int, str]
    ):
        return item in value
    elif ((type(value) is list) or (type(value) is tuple)) and (
        type(item) in [list, tuple]
    ):
        return item == value


def find_occurrences(tree: dict, desired_item) -> int:
    counter = 0

    # @print_debugger
    def recursion(tree: dict, item: str):
        nonlocal counter

        for key, value in tree.items():
            if key == item:
                counter += 1
            elif contains(value, item):
                counter += 1
            elif check_types(value, dict):
                idx = find_elements_indexes_by_type(value, dict)
                for _id in idx:
                    recursion(value[_id], item)
            elif type(value) is dict:
                recursion(value, item)
        return counter

    return recursion(tree, desired_item)


if __name__ == "__main__":
    # Example tree:
    example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "asd": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": ("RED", "Yello"),
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
        "RED": False,
        "False_key": 0,
        "deep_key": [{"no_red": "e", "blue": {"super_deep": "RED"}}],
    }

    item = "RED"

    print(find_occurrences(example_tree, item))  # 9

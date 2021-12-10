"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Function provides recursively search on given dict
    and counts occurrences of element.

    :param tree: A python dict
    :param element: An element (Any) which occurrences will be counted
    :rtype: inner counter's value
    """

    RECURSIVE_TYPES = tuple, list, set, dict
    counter = 0

    def recursive_search(tree: dict, element):
        nonlocal counter

        if type(tree) is type(element):
            if tree == element:
                counter += 1
                return

        if type(tree) not in RECURSIVE_TYPES:
            return

        _tree = tree.values() if type(tree) == dict else tree
        for leaf in _tree:
            recursive_search(tree=leaf, element=element)

        return counter

    return recursive_search(tree, element)


if __name__ == "__main__":

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

    print(find_occurrences(example_tree, ["RED", "BLUE"]))

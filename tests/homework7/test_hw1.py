from homework7.hw1 import find_occurrences

task_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

complex_tree = {
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
    "flag": False,
    "False_key": 0,
    "deep_key": [{"no_red": "e", "blue": {"super_deep": "RED"}}],
}


def test_task_tree_red_key():
    assert find_occurrences(task_tree, "RED") == 6


def test_complex_tree_red_key():
    assert find_occurrences(complex_tree, "RED") == 8


def test_complex_tree_blue_key():
    assert find_occurrences(complex_tree, "BLUE") == 2


def test_int_element_search():
    assert find_occurrences(complex_tree, 0) == 1


def test_bool_element_search():
    assert find_occurrences(complex_tree, False) == 1


def test_list_element_search():
    assert find_occurrences(complex_tree, ["RED", "BLUE"]) == 1

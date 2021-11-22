import string

from homework2.hw5 import make_custom_range


def test_positive_case1():
    assert make_custom_range(string.ascii_lowercase, "g") == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f"
        ]


def test_positive_case2():
    assert make_custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_positive_case3():
    assert make_custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_positive_case4():
    assert make_custom_range(range(0, 10), 5) == [0, 1, 2, 3, 4]


def test_negative_case1():
    assert not make_custom_range(string.ascii_lowercase, "g") == [
        "f",
        "a",
        "c",
        "d",
        "e",
        "f",
    ]


def test_negative_case2():
    assert not make_custom_range(
        string.ascii_lowercase, "a", "b"
        ) == ["a", "b"]


def test_negative_case3():
    assert not make_custom_range(range(1, 10), 1, 5, 1) == [1, 3, 4]


def test_negative_case4():
    assert not make_custom_range(range(1, 10), 1, 5, 2) == [1, 3, 5]

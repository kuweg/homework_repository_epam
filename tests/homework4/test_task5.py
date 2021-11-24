from typing import Generator

from homework4.task_5_optional import fizzbuzz


def test_5_fizzbuz():
    assert list(fizzbuzz(5)) == ["1", "2", "fizz", "4", "buzz"]


def test_10_fizzbuz():
    assert list(fizzbuzz(10)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
    ]


def test_15_fizzbuz():
    assert list(fizzbuzz(15)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizz buzz",
    ]


def test_isinstance_generator():
    a = fizzbuzz(5)
    assert isinstance(a, Generator) is True

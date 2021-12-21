import pytest

from homework9.hw2 import Suppressor, suppressor


def test_suppressor_generator():
    empty_list = []
    with suppressor(IndexError):
        empty_list[2]


def test_suppressor_class():
    empty_list = []
    with Suppressor(IndexError):
        empty_list[2]


def test_suppressor_class_errors():
    empty_list = []
    with Suppressor(IndexError, ZeroDivisionError, ValueError):
        empty_list[2]
        23 / 0
        int(False)


def test_irrelevant_exception():
    empty_list = []
    with pytest.raises(IndexError):
        try:
            with Suppressor(ValueError):
                empty_list[2]
        except IndexError:
            raise IndexError

import pytest

from homework9.hw2 import Suppressor, suppressor


def test_suppressor_generator():
    """Testing that specified exception is not raised."""
    empty_list = []
    with suppressor(IndexError):
        empty_list[2]


def test_suppressor_class():
    """Testing that specified exception is not raised."""
    empty_list = []
    with Suppressor(IndexError):
        empty_list[2]


def test_suppressor_specified_exception_generator():
    """Testing that specified exception is suppressed."""
    string = 'a'
    with pytest.raises(ValueError):
        with suppressor(IndexError):
            string = int(string)


def test_suppressor_specified_exception_class():
    """Testing that specified exception is suppressed."""
    string = 'a'
    with pytest.raises(ValueError):
        with Suppressor(IndexError):
            string = int(string)


def test_irrelevant_exception_class():
    """Testing that only specified expcetion will be suppressed."""
    empty_list = []
    with pytest.raises(IndexError):
        with Suppressor(ValueError):
            empty_list[2]


def test_irrelevant_exception_generator():
    """Testing that only specified expcetion will be suppressed."""
    empty_list = []
    with pytest.raises(IndexError):
        with suppressor(ValueError):
            empty_list[2]

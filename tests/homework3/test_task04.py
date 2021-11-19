import pytest

from homework3.task04 import is_armstrong


def test_raise_error():
    with pytest.raises(ValueError):
        is_armstrong(-1)


def test_positive_case1():
    assert is_armstrong(153) is True


def test_positive_case2():
    assert is_armstrong(407) is True


def test_positive_case3():
    assert is_armstrong(371) is True


def test_negative_case1():
    assert is_armstrong(12) is False


def test_negative_case2():
    assert is_armstrong(154) is False


def test_negative_case3():
    assert is_armstrong(408) is False

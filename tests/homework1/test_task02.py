from homework1.task02 import check_fibonacci



def test_positive_case1():
    "Testing that sequence given IS a Fibonacci sequence"
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


def test_positive_case2():
    "Testing that sequence given IS a Fibonacci sequence"
    assert check_fibonacci([0, 1])


def test_positive_case3():
    "Testing that sequence given IS a Fibonacci sequence"
    assert check_fibonacci([0])


def test_positive_case4():
    "Testing that sequence given IS a Fibonacci sequence"
    assert check_fibonacci([1, 1, 2])


def test_positive_case5():
    "Testing that sequence given IS a Fibonacci sequencen(tuple)"""
    assert check_fibonacci((1, 1))


def test_negative_case1():
    "Testing that sequence given IS a Fibonacci sequence with empty list"
    assert not check_fibonacci([])


def test_negative_case2():
    "Testing that sequence given IS NOT a Fibonacci sequence"
    assert not check_fibonacci([3, 4])


def test_negative_case3():
    "Testing that sequence given IS NOT a Fibonacci sequence"
    assert not check_fibonacci([0, 1, 2, 3, 4])


def test_negative_case4():
    "Testing that sequence given IS NOT a Fibonacci sequence"
    assert not check_fibonacci([1, -1, 2])


def test_negative_case5():
    "Testing that sequence given IS NOT a Fibonacci sequence"
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 53])
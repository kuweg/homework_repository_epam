from homework2.hw2 import major_and_minor_elem


def test_positive_case1():
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_positive_case2():
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_positive_case3():
    assert major_and_minor_elem([4, 4, 4, 2, 6, 3, 2, 6]) == (None, 3)


def test_negative_case1():
    assert not major_and_minor_elem([1, 1, 1, 2, 2, 3]) == (2, 3)


def test_negative_case2():
    assert not major_and_minor_elem([4, 4, 4, 2, 6, 3, 2, 6]) == (4, 3)

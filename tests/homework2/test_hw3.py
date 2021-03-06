from homework2.hw3 import make_combinations


def test_positive_case1():
    assert make_combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_positive_case2():
    assert make_combinations([2, 3, 4], [2, 3, 4]) == [
        [2, 2],
        [2, 3],
        [2, 4],
        [3, 2],
        [3, 3],
        [3, 4],
        [4, 2],
        [4, 3],
        [4, 4],
    ]


def test_negative_case1():
    assert not make_combinations([], []) == [1]


def test_negative_case2():
    assert not make_combinations([2], [1]) == [1, 2]

from homework1.task05 import find_maximal_subarray_sum


def test_positive_case1():
    "Test that function finds max sum subarray correct"
    assert find_maximal_subarray_sum([1, 2, -3, 4, -5, 6, 7, 8], 3) == 21


def test_positive_case2():
    "Test that function finds max sum subarray correct"
    assert find_maximal_subarray_sum([1, 2, -3, -4, 5, 6, 7, 8], 4) == 26


def test_positive_case3():
    "Test that function finds max sum subarray correct"
    assert find_maximal_subarray_sum([1, 2, 3, 4, 5, 6, 7, 8], 1) == 8


def test_positive_case4():
    "Test that function finds max sum subarray correct"
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_positive_case5():
    "Test that function finds max sum subarray correct"
    assert find_maximal_subarray_sum([1, -3, -1, -3, -5, -3, -6, -7], 1) == 1


def test_negaive_case1():
    "Test that function returns int"
    assert not type(find_maximal_subarray_sum(
        [1, 2, 3, 4, 5, 6, 7, 8], 1)
        ) != int


def test_negaive_case2():
    "Test that function finds max sum subarray correct"
    assert not find_maximal_subarray_sum([1, 2, 3, 4, 5, 6, 7, 8], 1) == 0


def test_negaive_case3():
    "Test that function finds max sum subarray correct"
    assert not find_maximal_subarray_sum([1, 2, 3, 4, 5, 6, 7, 8], 1) != 8

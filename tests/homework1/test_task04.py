from homework1.task04 import check_sum_of_four



def test_positive_case1():
    'Test taht function finds number of tuples correctly'
    assert check_sum_of_four([1, 0], [2, 3], [-1,0], [-2, 3]) == 3


def test_positive_case2():
    'Test taht function finds number of tuples correctly'
    assert check_sum_of_four([1,2], [3,4], [5,6], [7, 8]) == 0


def test_positive_case3():
    'Test taht function finds number of tuples correctly'
    assert check_sum_of_four([89, 1], [1,0], [-89, 27], [-1, -3]) == 1


def test_positive_case4():
    'Test taht function finds number of tuples correctly'
    assert (check_sum_of_four([1, 0, 3], [1, 5, 3], [-1, 0, 4], [-1, -2, 4])) == 4


def test_negative_case1():
    'Checking a result form test_positive_case2'
    assert not check_sum_of_four([1,2],[3,4],[5,6],[7, 8]) == 1


def test_negative_case2():
    'Test taht function finds number of tuples correctly'
    assert not check_sum_of_four([89, 1], [1,0], [-89, 27], [-1, -3]) == 4


def test_negative_case3():
    'Test taht function finds number of tuples correctly'
    assert not check_sum_of_four([1, 1, 1], [1, 1, 1], [-1, -1, -1], [-1, -1, -1]) != 81
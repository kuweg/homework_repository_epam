from homework1.task03 import find_maximum_and_minimum

"""
Files were generated with random.randint(-100, 100)
"""


def test_positive_case1():
    assert find_maximum_and_minimum(
        'tests/homework1/task03_test_data_0.txt') == (-90, 100)


def test_positive_case2():
    assert find_maximum_and_minimum(
        'tests/homework1/task03_test_data_1.txt') == (-82, 93)


def test_positive_case3():
    assert find_maximum_and_minimum(
        'tests/homework1/task03_test_data_2.txt') == (-100, 100)


def test_positive_case4():
    assert find_maximum_and_minimum(
        'tests/homework1/task03_test_data_3.txt') == (-96, 100)

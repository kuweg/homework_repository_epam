from homework1.calc import check_if_power_of_2


def test_positive_case1():
    """Testing that actual powers of 2 give True"""
    assert check_if_power_of_2(65536)


def test_positive_case2():
    """Testing that actual powers of 2 give True"""
    assert check_if_power_of_2(2147483648)


def test_positive_case3():
    """Testing that actual powers of 2 give True"""
    assert check_if_power_of_2(4294967296)


def test_negative_case1():
    """Testing that non-powers of 2 give False"""
    assert not check_if_power_of_2(12)


def test_negative_case2():
    """Testing that non-powers of 2 give False"""
    assert not check_if_power_of_2(25)


def test_negative_case3():
    """Testing that non-powers of 2 give False"""
    assert not check_if_power_of_2(4294967295)

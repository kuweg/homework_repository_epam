from homework7.hw2 import backspace_compare


def test_positive_case_1():
    s1 = "ab#c"
    s2 = "ad#c"
    assert backspace_compare(s1, s2) is True


def test_positive_case_2():
    s1 = "a##c"
    s2 = "#a#c"
    assert backspace_compare(s1, s2) is True


def test_positive_case_3():
    s1 = "a#c"
    s2 = "b"
    assert backspace_compare(s1, s2) is False

from datetime import datetime

from homework7.hw2 import backspace_compare
from homework7.hw2_slow_solution import backspace_compare_slow


def _read_file(file_path):
    string = []
    with open(file_path, 'r') as file:
        for line in file:
            string.append(line.strip())
    string = string[0]
    return string


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


def test_speed_test(capsys):
    long_str_1 = _read_file('tests/homework7/text1.txt')
    long_str_2 = _read_file('tests/homework7/text2.txt')

    start1 = datetime.now()
    _ = backspace_compare_slow(long_str_1, long_str_2)
    end1 = datetime.now() - start1

    start2 = datetime.now()
    _ = backspace_compare(long_str_1, long_str_2)
    end2 = datetime.now() - start2

    assert end2.total_seconds() < end1.total_seconds()

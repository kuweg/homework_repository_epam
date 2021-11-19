from homework2.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                           get_longest_diverse_words,
                           get_most_common_non_ascii_char, get_rarest_char)

test_data1_path = "tests/homework2/test_data_hw1_1.txt"
test_data2_path = "tests/homework2/test_data_hw1_2.txt"
encoding = "unicode-escape"
error_handler = "ignore"


def test_get_longest_diverse_words():
    assert get_longest_diverse_words(
        test_data1_path, encoding,
        error_handler
        ) == [
        "123456789",
        "12345678",
        "123456",
        "1222345",
        "12345",
        "12",
        "123",
        "221",
        "1111",
        "11",
    ]


def test_get_rarest_char():
    assert get_rarest_char(
        test_data1_path, encoding,
        error_handler
        ) == "9"


def test_count_punctuation_chars():
    assert count_punctuation_chars(
        test_data1_path, encoding,
        error_handler
        ) == 3


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(
        test_data2_path, encoding,
        error_handler
        ) == 12


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(
        test_data2_path, encoding,
        error_handler
        ) == "㪘"

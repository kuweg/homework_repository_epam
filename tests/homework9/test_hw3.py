import pathlib

from homework9.hw3 import universal_file_counter

cwd = "./tests/homework9"
cwd_test3 = cwd + "/complex_file"
DIR_PATH = pathlib.Path(cwd)
DIR_PATH2 = pathlib.Path(cwd_test3)
EXTENSION = "txt"


def test_case_none_tokenizer():
    """
    Testing counter without tokenizer. Assuming that it will return
    line counts.
    """
    assert (
        universal_file_counter(
            dir_path=DIR_PATH, file_extension=EXTENSION, tokenizer=None
        )
        == 6
    )


def test_case_split_tokenizer():
    """Testing counter with tokenizer str.split()."""
    assert (
        universal_file_counter(
            dir_path=DIR_PATH, file_extension=EXTENSION, tokenizer=str.split
        )
        == 6
    )


def test_split_tokenizer_with_complex_file():
    """Testing that coounter will wokr with more comples file structure."""
    assert (
        universal_file_counter(
            dir_path=DIR_PATH2, file_extension=EXTENSION, tokenizer=str.split
        )
        == 16
    )


def test_split_tokenizer_negative():
    """Testing that previuos test was correct."""
    assert not (
        universal_file_counter(
            dir_path=DIR_PATH2, file_extension=EXTENSION, tokenizer=str.split
        )
        == 8
    )

import os
import pathlib

from homework9.hw3 import universal_file_counter

cwd = os.getcwd() + "/homework9"
DIR_PATH = pathlib.Path(cwd)
EXTENSION = "txt"


def test_case_none_tokenizer():

    assert (
        universal_file_counter(
            dir_path=DIR_PATH, file_extension=EXTENSION, tokenizer=None
        )
        == 6
    )


def test_case_split_tokenizer():
    assert (
        universal_file_counter(
            dir_path=DIR_PATH, file_extension=EXTENSION, tokenizer=str.split
        )
        == 6
    )

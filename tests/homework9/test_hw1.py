import os

import pytest

from homework9.hw1 import merge_sorted_files
from homework9.utils.dummy_int import DummyIntegers

dummy = DummyIntegers(n_files=2,
                      template_name="tfile",
                      file_size=5,
                      seed=True)

dummy_small = DummyIntegers(n_files=2,
                            template_name="sfile",
                            file_size=2,
                            seed=True)


@pytest.fixture()
def set_chdir():
    os.chdir("tests/homework9")


@dummy
def test_case_1():
    files = dummy.get_paths()
    assert list(merge_sorted_files(files)) == [0, 2, 4, 4, 6, 6, 7, 7, 10, 10]


@dummy_small
def test_case_2():
    files = dummy_small.get_paths()
    assert list(merge_sorted_files(files)) == [2, 3, 8, 9]

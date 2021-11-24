import os
from typing import Any, Callable, List

import pytest

from homework4.task_1_read_file import read_magic_number

file_name = "test_file.txt"
dummy_file = "dummy_file.txt"


@pytest.fixture
def set_chdir():
    os.chdir("tests/homework4")


def _test_file_existance(file_name: str) -> bool:
    if file_name in os.listdir():
        return True
    return False


def _create_file_with_numbers(
    file_name: str, data_to_write: List[Any], rewrite: bool = False
):
    if not _test_file_existance(file_name) or rewrite:
        with open(file_name, "w") as file_handler:
            for number in data_to_write:
                file_handler.write(str(number) + "\n")


def _manipulate_dummy_file(file_name: str, create_or_delete: bool):
    if create_or_delete:
        dummy_file = open(file_name, "w")
        dummy_file.close()
    else:
        if _test_file_existance(file_name):
            os.remove(file_name)


def remove_file_decorator(file_name: str):
    def outer(func: Callable):
        def wrapper():
            func()
            if _test_file_existance(file_name):
                os.remove(file_name)
        return wrapper
    return outer


@remove_file_decorator(file_name)
def test_first_number_in_range():
    _create_file_with_numbers(file_name, [2, 5, 5, 4], True)
    assert read_magic_number(file_name) is True


@remove_file_decorator(file_name)
def test_first_number_not_in_range():
    _create_file_with_numbers(file_name, [10, 1, 1, 1], True)
    assert read_magic_number(file_name) is False


@remove_file_decorator(file_name)
def test_value_error():
    _create_file_with_numbers(file_name, ["a", 1])
    with pytest.raises(ValueError):
        read_magic_number(file_name)


def test_file_exists_error():
    with pytest.raises(FileExistsError):
        read_magic_number('text.txt')


def test_file_deleting_positive():
    file_list_before_test = os.listdir()
    test_first_number_in_range()
    file_list_after_test = os.listdir()
    assert file_list_before_test == file_list_after_test


def test_file_deleting_negative():
    file_list_before = os.listdir()
    _manipulate_dummy_file(dummy_file, True)
    test_first_number_in_range()
    file_list_after = os.listdir()
    _manipulate_dummy_file(dummy_file, False)
    assert not file_list_before == file_list_after

from unittest import mock

import pytest

from homework4.task_2_mock_input import count_dots_on_i


def test_example_from_task():
    assert count_dots_on_i("https://example.com/") == 59


def test_exception():
    with pytest.raises(ValueError):
        count_dots_on_i("httpd://example.com")


@mock.patch("homework4.task_2_mock_input.open_url", return_value="iii")
def test_answer(mock):
    assert count_dots_on_i("https://example.com/") == 3

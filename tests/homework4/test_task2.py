from unittest import mock

import pytest

from homework4.task_2_mock_input import count_dots_on_i

with open("tests/homework4/Example_Domain.html", "r") as html:
    mock_data = html.read()


# Mocking a return form open_url() with a saved copy
# of url's web-page from task description.
@mock.patch("homework4.task_2_mock_input.open_url", return_value=mock_data)
def test_example_from_task(mock):
    assert count_dots_on_i("https://example.com/") == 59


def test_exception():
    with pytest.raises(ValueError):
        count_dots_on_i("httpd://example.com")


@mock.patch("homework4.task_2_mock_input.open_url", return_value="iii")
def test_answer(mock):
    assert count_dots_on_i("https://example.com/") == 3

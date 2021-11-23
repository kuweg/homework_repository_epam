"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""

from urllib.error import URLError
from urllib.request import urlopen


def open_url(url: str):
    """
    Opens a url using urlib module.
    https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
    """
    try:
        data_from_url = urlopen(url).read().decode("utf-8")
        return data_from_url
    except URLError:
        raise ValueError(f"Unreachable {url}")


def count_dots_on_i(url: str) -> int:
    """
    Return count of 'i' symbol from web page.
    """
    url_data = open_url(url)
    i_counts = url_data.count("i")
    return i_counts

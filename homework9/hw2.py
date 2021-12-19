"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager
from typing import Any, Generator


class Suppressor:
    """
    Context manager class that suppresses passed exception.

    :param exception: any exception
    :type exception: exception
    """

    def __init__(self, *exceptions: Exception) -> None:
        self.exceptions = exceptions

    def __enter__(self) -> None:
        pass

    def __exit__(self, ex_type: Exception, *args: Any) -> bool:
        return ex_type in self.exceptions


@contextmanager
def suppressor(exceptions: Exception) -> Generator:
    """
    A Generator function  that suppresses passed exception.
    """
    try:
        yield
    except exceptions:
        pass


if __name__ == "__main__":
    a = []
    with Suppressor(IndexError):
        a[2]

    with suppressor(IndexError):
        a[3]

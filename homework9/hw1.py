"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    Merges ant amount of sorted files with int values
    and sort them as iterator.

    :param file_list: list of files paths
    :type file_list: list[str]
    :return: iterator object
    """

    files = [open(fname, "r") for fname in file_list]

    yield from (
        int(num.rstrip()) for num
        in heapq.merge(*files, key=lambda x: int(x.rstrip()))
    )

    for file_object in files:
        file_object.close()

"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp_list: List) -> Tuple[int, int]:
    """
    Finding most common and least common elements
    in list using collections.Counter.
    collectins.Counter docs:
    https://docs.python.org/3/library/collections.html#collections.Counter
    """
    counter = Counter(inp_list)
    counts = counter.most_common()
    most_common = counts[0][0]
    most_common_count = counts[0][1]
    least_common = counts[-1][0]
    if most_common_count <= len(inp_list) // 2:
        most_common = None
    return most_common, least_common

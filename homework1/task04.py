"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    """
    Counting amount of tuples according rule:
     (A[i] + B[j] + C[k] + D[l]) == 0.
    """

    # Using dict because it is a O(1) to check a values.
    # Similar to TwoSum from LeetCode
    sums = {}
    counter = 0
    for elem_a in a:
        for elem_b in b:
            sums[elem_a + elem_b] = sums.get(elem_a + elem_b, 0) + 1
    for elem_c in c:
        for elem_d in d:
            if (elem_c + elem_d) * -1 in sums:
                counter += sums[(elem_c + elem_d) * -1]
    return counter

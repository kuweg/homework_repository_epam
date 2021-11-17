"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Finding maximum sum of subarray whith stated length.
    """
    max_n = 0
    for i in range(len(nums) - k + 1):
        current_slice = nums[i: i + k]
        if sum(current_slice) > max_n:
            max_n = sum(current_slice)
    return max_n

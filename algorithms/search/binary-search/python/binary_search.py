"""Binary search.

[Time-Complexity]: O(n log2{n})

[Space-Complexity]: O(1)
"""
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def binary_search(items: Sequence[T], target: T) -> int:
    """Binary search.

    Args:
        items: A sorted sequence of elements.
        target: Searching element in given sequence.

    Returns:
        Index of target in sequence, else -1.

    """
    if not len(items):
        return -1

    left = 0
    right = len(items)

    while left + 1 < right:
        m = left + (right - left) // 2
        if items[m] > target:
            right = m
        else:
            left = m

    return left if items[left] == target else -1

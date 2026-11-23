"""Binary search.

[Time-Complexity]: O(log n) with constant-time indexing

[Space-Complexity]: O(1)
"""
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def binary_search(items: Sequence[T], target: T) -> int:
    """Binary search.

    Args:
        items: A nondecreasing sequence with constant-time indexing.
        target: Element to find in the sequence.

    Returns:
        Rightmost index of target, or -1 if absent.

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

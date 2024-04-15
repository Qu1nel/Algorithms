"""Jump to search.

[Time-Complexity]: O(sqrt(n))

[Space-Complexity]: O(1)
"""
from collections.abc import Sequence
from math import sqrt
from typing import TypeVar

T = TypeVar("T")


def jump_search(items: Sequence[T], target: T) -> int:
    """Jump to search.

    Args:
        items: A sorted sequence of elements.
        target: Searching element in given sequence.

    Returns:
        Index of target in sequence, else -1.

    """
    if not (n := len(items)):
        return -1

    step = int(sqrt(n))

    left = right = 0
    is_found = False

    for idx in range(0, n, step):
        left = idx
        right = min(n - 1, left + step)

        if items[left] <= target <= items[right]:
            is_found = True
            break

    if not is_found:
        return -1

    l, r = left, right + 1

    while l + 1 < r:
        m = l + (r - l) // 2
        if items[m] > target:
            r = m
        else:
            l = m

    return l if items[l] == target else -1
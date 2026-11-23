"""Jump search with binary search inside the selected block.

[Time-Complexity]: O(sqrt(n))

[Space-Complexity]: O(1)
"""
from collections.abc import Sequence
from math import isqrt
from typing import TypeVar

T = TypeVar("T")


def jump_search(items: Sequence[T], target: T) -> int:
    """Find a target by jumping between blocks.

    Args:
        items: A nondecreasing sequence with constant-time indexing.
        target: Element to find in the sequence.

    Returns:
        Rightmost matching index in the first candidate block, or -1.

    """
    if not (n := len(items)):
        return -1

    step = isqrt(n)

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

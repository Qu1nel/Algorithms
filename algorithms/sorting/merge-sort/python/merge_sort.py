"""Merge sort.

[Worst Time-Complexity]: O(n log2{n})
[Best Time-Complexity]: Omega(n log2{n})
[AVG Time-Complexity]: Theta(n log2{n})

[Space-Complexity]: O(n) | O(1) - linked list

"""
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def swap_in(items: Sequence[T], idx_1: int, idx_2: int) -> None:
    """Swap elements 'idx_1' and 'idx_2' in 'items'."""
    items[idx_1], items[idx_2] = items[idx_2], items[idx_1]


def merge_sort(data: Sequence[T]) -> Sequence[T]:
    """Merge sorting.

    Args:
        data: A Sequence of element type T

    Returns:
        Sorted given sequence.

    """
    if len(data) <= 1:
        return data

    avg = len(data) // 2

    left = merge_sort(data[:avg])
    right = merge_sort(data[avg:])

    n, m = len(left), len(right)
    i = k = 0

    result = []

    while i < n and k < m:
        if left[i] < right[k]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[k])
            k += 1

    result += left[i:] + right[k:]
    return result

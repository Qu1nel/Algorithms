"""Insert sort.

[Worst Time-Complexity]: O(n^2)
[Best Time-Complexity]: O(n)
[AVG Time-Complexity]: O(n^2)

[Space-Complexity]: O(n) | O(1)

"""
from collections.abc import Sequence
from copy import deepcopy
from typing import TypeVar

T = TypeVar("T")


def swap_in(items: Sequence[T], idx_1: int, idx_2: int) -> None:
    """Swap elements 'idx_1' and 'idx_2' in 'items'."""
    items[idx_1], items[idx_2] = items[idx_2], items[idx_1]


def insert_sort(items: Sequence[T]) -> Sequence[T]:
    """Insert sorting.

    Args:
        items: A Sequence of element type T

    Returns:
        Sorted given sequence.

    """
    n = len(items)
    items_copy = deepcopy(items)

    for i in range(1, n):
        k = i
        while k != 0 and items_copy[k] < items_copy[k - 1]:
            swap_in(items_copy, k, k - 1)
            k -= 1

    return items_copy

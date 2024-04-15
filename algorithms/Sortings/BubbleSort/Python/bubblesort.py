"""Bubble sort.

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


def bubble_sort(items: Sequence[T]) -> Sequence[T]:
    """Bubble sorting.

    Args:
        items: A Sequence of element type T

    Returns:
        Sorted given sequence.

    """
    n = len(items)
    items_copy = deepcopy(items)

    for k in range(n - 1):
        for i in range(n - k - 1):
            if items_copy[i] > items_copy[i + 1]:
                swap_in(items_copy, i + 1, i)

    return items_copy

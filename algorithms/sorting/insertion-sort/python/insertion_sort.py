"""Insertion sort.

[Worst Time-Complexity]: O(n^2)
[Best Time-Complexity]: O(n)
[AVG Time-Complexity]: O(n^2)

[Space-Complexity]: O(n) including the returned copy; O(1) beyond it

"""
from collections.abc import MutableSequence, Sequence
from typing import TypeVar

T = TypeVar("T")


def swap_in(items: MutableSequence[T], idx_1: int, idx_2: int) -> None:
    """Swap elements 'idx_1' and 'idx_2' in 'items'."""
    items[idx_1], items[idx_2] = items[idx_2], items[idx_1]


def insert_sort(items: Sequence[T]) -> list[T]:
    """Sort a sequence by inserting items into a sorted prefix.

    Args:
        items: A Sequence of element type T

    Returns:
        A new sorted list containing the original elements.

    """
    n = len(items)
    items_copy = list(items)

    for i in range(1, n):
        k = i
        while k != 0 and items_copy[k] < items_copy[k - 1]:
            swap_in(items_copy, k, k - 1)
            k -= 1

    return items_copy

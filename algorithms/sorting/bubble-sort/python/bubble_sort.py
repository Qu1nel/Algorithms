"""Bubble sort.

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


def bubble_sort(items: Sequence[T]) -> list[T]:
    """Bubble sorting.

    Args:
        items: A Sequence of element type T

    Returns:
        A new sorted list containing the original elements.

    """
    n = len(items)
    items_copy = list(items)

    for k in range(n - 1):
        swapped = False
        for i in range(n - k - 1):
            if items_copy[i] > items_copy[i + 1]:
                swap_in(items_copy, i + 1, i)
                swapped = True
        if not swapped:
            break

    return items_copy

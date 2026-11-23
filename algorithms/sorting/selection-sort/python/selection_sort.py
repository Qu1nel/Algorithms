"""Selection sort.

[Worst Time-Complexity]: O(n^2)
[Best Time-Complexity]: O(n^2)
[AVG Time-Complexity]: O(n^2)

[Space-Complexity]: O(n) including the returned copy; O(1) beyond it

"""
from collections.abc import MutableSequence, Sequence
from typing import TypeVar

T = TypeVar("T")


def swap_in(items: MutableSequence[T], idx_1: int, idx_2: int) -> None:
    """Swap elements 'idx_1' and 'idx_2' in 'items'."""
    items[idx_1], items[idx_2] = items[idx_2], items[idx_1]


def selection_sort(items: Sequence[T]) -> list[T]:
    """Selection sorting.

    Args:
        items: A Sequence of element type T

    Returns:
        A new sorted list containing the original elements.

    """
    n = len(items)
    items_copy = list(items)

    for k in range(n - 1):
        smallest = k

        for i in range(k + 1, n):
            if items_copy[smallest] > items_copy[i]:
                smallest = i

        if smallest != k:
            swap_in(items_copy, smallest, k)

    return items_copy

"""Comb sort.

[Worst Time-Complexity]: O(n^2)
[Best Time-Complexity]: Theta(n log n)

[Space-Complexity]: O(n) including the returned copy; O(1) beyond it

"""
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def comb_sort(items: Sequence[T]) -> list[T]:
    """Comb sorting.

    Args:
        items: A Sequence of element type T

    Returns:
        A new sorted list containing the original elements.

    """
    items_copy = list(items)
    n = len(items_copy)
    step = n
    swapped = False

    while step > 1 or swapped:
        step = max(1, step * 1000 // 1247)
        swapped = False
        for i in range(n - step):
            if items_copy[i] > items_copy[i + step]:
                items_copy[i], items_copy[i + step] = items_copy[i + step], items_copy[i]
                swapped = True

    return items_copy

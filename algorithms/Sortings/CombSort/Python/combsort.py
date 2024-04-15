"""Comb sort.

[Worst Time-Complexity]: O(n^2)
[Best Time-Complexity]: Theta(n log2{n})
[AVG Time-Complexity]: Omega(n^2 / P^2), where P - count steps

[Space-Complexity]: O(n) | O(1)

"""
from collections.abc import Sequence
from copy import deepcopy
from typing import TypeVar

T = TypeVar("T")


def swap_in(items: Sequence[T], idx_1: int, idx_2: int) -> None:
    """Swap elements 'idx_1' and 'idx_2' in 'items'."""
    items[idx_1], items[idx_2] = items[idx_2], items[idx_1]


def comb_sort(items: Sequence[T]) -> Sequence[T]:
    """Comb sorting.

    Args:
        items: A Sequence of element type T

    Returns:
        Sorted given sequence.

    """
    items_copy = deepcopy(items)
    n = len(items_copy)
    k = 1.247
    step = int(n / k)

    swap_count = 1

    while step > 1 or swap_count > 0:
        swap_count = 0
        i = 0

        while i + step < n:
            if items_copy[i] > items_copy[i + step]:
                items_copy[i], items_copy[i + step] = items_copy[i + step], items_copy[i]
                swap_count += 1

            i += 1

        step = int(step / k) if step > 1 else step

    return items_copy

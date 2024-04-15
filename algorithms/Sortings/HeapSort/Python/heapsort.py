"""Heap sort.

[Worst Time-Complexity]: O(n log2{n})
[Best Time-Complexity]: O(n log2{n})
[AVG Time-Complexity]: O(n log2{n})

[Space-Complexity]: O(n) | O(1)

"""
from collections.abc import Sequence
from copy import deepcopy
from typing import TypeVar

T = TypeVar("T")


def swap_in(items: Sequence[T], idx_1: int, idx_2: int) -> None:
    """Swap elements 'idx_1' and 'idx_2' in 'items'."""
    items[idx_1], items[idx_2] = items[idx_2], items[idx_1]


def heap_sort(data: Sequence[T]) -> Sequence[T]:
    """Heap sorting.

    Args:
        data: A Sequence of element type T

    Returns:
        Sorted given sequence.

    """
    data_copy = deepcopy(data)
    length = len(data_copy)

    def heapify(data_: Sequence, n: int, i: int) -> None:
        """Converts a list to a binary heap."""
        largest = i
        left: int = 2 * i + 1
        right: int = 2 * i + 2

        if left < n and data_[i] < data_[left]:
            largest = left

        if right < n and data_[largest] < data_[right]:
            largest = right

        if largest != i:
            swap_in(data_, i, largest)
            heapify(data_, n, largest)

    for i in range(length, -1, -1):
        heapify(data_copy, length, i)

    for i in range(length - 1, 0, -1):
        swap_in(data_copy, i, 0)
        heapify(data_copy, i, 0)

    return data_copy

"""Heap sort.

[Worst Time-Complexity]: O(n log2{n})
[Best Time-Complexity]: O(n) when all keys are equal
[AVG Time-Complexity]: O(n log2{n})

[Space-Complexity]: O(n) including the returned copy; O(1) beyond it

"""
from collections.abc import MutableSequence, Sequence
from typing import TypeVar

T = TypeVar("T")


def swap_in(items: MutableSequence[T], idx_1: int, idx_2: int) -> None:
    """Swap elements 'idx_1' and 'idx_2' in 'items'."""
    items[idx_1], items[idx_2] = items[idx_2], items[idx_1]


def heap_sort(data: Sequence[T]) -> list[T]:
    """Heap sorting.

    Args:
        data: A Sequence of element type T

    Returns:
        A new sorted list containing the original elements.

    """
    data_copy = list(data)
    length = len(data_copy)

    def sift_down(n: int, i: int) -> None:
        """Restore the max-heap property below an index."""
        while (child := 2 * i + 1) < n:
            if child + 1 < n and data_copy[child] < data_copy[child + 1]:
                child += 1
            if not data_copy[i] < data_copy[child]:
                return
            swap_in(data_copy, i, child)
            i = child

    for i in range(length // 2 - 1, -1, -1):
        sift_down(length, i)

    for i in range(length - 1, 0, -1):
        swap_in(data_copy, i, 0)
        sift_down(i, 0)

    return data_copy

"""Merge sort.

[Worst Time-Complexity]: O(n log2{n})
[Best Time-Complexity]: Omega(n log2{n})
[AVG Time-Complexity]: Theta(n log2{n})

[Space-Complexity]: O(n) peak additional memory, including slices and result

"""
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def merge_sort(data: Sequence[T]) -> list[T]:
    """Merge sorting.

    Args:
        data: A Sequence of element type T

    Returns:
        A new sorted list. Equal keys retain their input order.

    """
    def sort(items: list[T]) -> list[T]:
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = sort(items[:mid])
        right = sort(items[mid:])
        i = j = 0
        result: list[T] = []

        while i < len(left) and j < len(right):
            if right[j] < left[i]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return sort(list(data))

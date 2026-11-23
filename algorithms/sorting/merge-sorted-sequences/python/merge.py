"""Merge two sorted sequences.

[Time-Complexity]: O(n + m) for merge; up to O((n + m)^2) for merge_sequence on lists

[Space-Complexity]: O(n + m) for the returned list
"""

from collections.abc import MutableSequence, Sequence
from typing import TypeVar

T = TypeVar("T")


def merge_sequence(a: MutableSequence[T], b: MutableSequence[T]) -> list[T]:
    """Merge by taking elements from the fronts of mutable inputs.

    Args:
        a: First nondecreasing sequence. Its consumed prefix is removed.
        b: Second nondecreasing sequence. Its consumed prefix is removed.

    Returns:
        A new list with every element in order. Take from b first on ties.
    """
    result: list[T] = []
    while a and b:
        el = a.pop(0) if a[0] < b[0] else b.pop(0)
        result.append(el)

    result.extend(b)
    result.extend(a)
    return result


def merge(a: Sequence[T], b: Sequence[T]) -> list[T]:
    """Merge by indexing the two inputs.

    Args:
        a: First nondecreasing sequence with constant-time indexing.
        b: Second nondecreasing sequence with constant-time indexing.

    Returns:
        A new list with every element in order. Take from b first on ties.
    """
    result: list[T] = []
    n, m = len(a), len(b)
    i, j = 0, 0

    while i != n and j != m:
        if a[i] < b[j]:
            el = a[i]
            i += 1
        else:
            el = b[j]
            j += 1

        result.append(el)

    result.extend(a[index] for index in range(i, n))
    result.extend(b[index] for index in range(j, m))
    return result

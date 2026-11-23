"""Randomized three-way quicksort with an explicit work stack.

[Worst Time-Complexity]: O(n^2)
[Best Time-Complexity]: O(n) when all keys are equal
[AVG Time-Complexity]: O(n log n) in expectation over pivot choices

[Space-Complexity]: O(n)

"""
import random
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def quick_sort(data: Sequence[T]) -> list[T]:
    """Sort a sequence by stable three-way partitioning.

    Args:
        data: A sequence of comparable elements.

    Returns:
        A new sorted list. Equal keys retain their input order.

    """
    result: list[T] = []
    pending = [(False, list(data))]
    while pending:
        ready, items = pending.pop()
        if ready or len(items) < 2:
            result.extend(items)
            continue

        pivot = random.choice(items)
        lower: list[T] = []
        equal: list[T] = []
        upper: list[T] = []

        for item in items:
            if item < pivot:
                lower.append(item)
            elif pivot < item:
                upper.append(item)
            else:
                equal.append(item)

        # A stack processes the lower partition before the equal and upper runs.
        if upper:
            pending.append((False, upper))
        pending.append((True, equal))
        if lower:
            pending.append((False, lower))

    return result

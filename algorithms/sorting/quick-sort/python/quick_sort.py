"""Quick sort recursive.

[Worst Time-Complexity]: O(n^2)
[Best Time-Complexity]: O(n log2{n}) | O(n) - for three divisions
[AVG Time-Complexity]: O(n log2{n})

[Space-Complexity]: O(n)

"""
import random
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def quick_sort(data: Sequence[T]) -> Sequence[T]:
    """Quick sorting based on recursion.

    Args:
        data: A some sequence of elemets type T.

    Returns:
        Sorted given sequence.

    """
    n = len(data)

    if n <= 1:
        return data

    middle = data[random.randint(0, n - 1)]

    center = []
    lower = []
    bigger = []

    for num in data:
        if num == middle:
            center.append(num)
        elif num < middle:
            lower.append(num)
        else:
            bigger.append(num)

    return quick_sort(lower) + center + quick_sort(bigger)

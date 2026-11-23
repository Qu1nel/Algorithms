"""Trial division using the 6k ± 1 candidates.

[Time-Complexity]: O(√n)

[Space-Complexity]: O(1)

The test is based on the fact that all prime numbers greater than 3 are of the form 6k ± 1, where k is any integer
greater than 0.
"""

import math


def is_prime(number: int) -> bool:
    """Check whether an integer is prime.

    Checks number, whether n is divisible by 2 or 3, and then checks all numbers of the form 6k ± 1 <= √n

    Args:
        number: Integer to test.

    Returns:
        True if number is prime, otherwise False.

    """
    if number <= 3:
        return number > 1

    if number % 3 == 0 or number % 2 == 0:
        return False

    for i in range(5, math.isqrt(number) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

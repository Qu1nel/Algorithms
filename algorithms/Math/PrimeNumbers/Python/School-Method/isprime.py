"""School-Method primality test.

[Time-Complexity]: O(√n)

[Space-Complexity]: O(1)

The test is based on the fact that all prime numbers greater than 3 are of the form 6k ± 1, where k is any integer
greater than 0.
"""

import math


def is_prime(number: int) -> bool:
    """The function checks number for simplicity in time O(√n).

    Checks number, whether n is divisible by 2 or 3, and then checks all numbers of the form 6k ± 1 <= √n

    Args:
        number: is the number to be tested.

    Returns:
        True if the number is probably prime else False

    Raises:
        AssertionError: is number < 1

    """
    assert number > 0, "Number < 1 not valid"

    if number <= 3:
        return number > 1

    if number % 3 == 0 or number % 2 == 0:
        return False

    for i in range(5, int(math.sqrt(number)), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

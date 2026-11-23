"""Miller-Rabin primality test.

[Time-Complexity]: O(k log n) modular multiplications

[Space-Complexity]: O(1) large integers; see README for the bit model


For odd composite n and independent uniform bases, at most one quarter of
the bases are strong liars in each round.
"""

import random


def miller_rabin_test(d: int, number: int) -> bool:
    """Miller-Rabin Primality Test.

    Tests the number for the possibility of simplicity.

    Args:
        number: is the number to be tested.
        d: is an odd number such that (n - 1) can be written in the form of (d * 2^r).

    Returns:
        True if the number is probably prime else False

    """
    a = random.randrange(2, number - 1)
    x = pow(a, d, number)

    if x in (1, number - 1):
        return True

    d *= 2
    while d < number - 1:
        x = (x * x) % number

        if x == 1:
            return False
        if x == number - 1:
            return True
        d *= 2

    return False


def is_prime(number: int, k: int) -> bool:
    """Probabilistic test of number for simplicity using the Miller-Rabin test.

    Args:
        number: is the number to be tested.
        k: Positive number of independent random rounds for odd candidates.

    Raises:
        ValueError: If k is less than one.

    Returns:
        True if the number is probably prime else False

    """
    if k < 1:
        raise ValueError("k must be positive")
    if number <= 3:
        return number >= 2
    if number % 2 == 0:
        return False

    d = number - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        if not miller_rabin_test(d, number):
            return False

    return True

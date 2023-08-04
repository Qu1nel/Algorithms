"""Miller-Rabin primality test.

[Time-Complexity]: O(k * log^3(p))

[Space-Complexity]: O(1)


According to Rabin's theorem, the probability that a randomly chosen number a witnesses the simplicity of a composite
number is approximately 1/4.

Hence, if we check k random numbers a, the probability of accepting a composite number as prime is ~(1/4)^k.

The complexity of the algorithm is O(k * log^3 * p), where k is the number of checks.
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
    a = 2 + random.randint(1, number - 4)
    x = pow(a, d, number)

    if x in (1, number - 1):
        return True

    while d != number - 1:
        x = (x * x) % number
        d *= 2

        if x == 1:
            return False
        if x == number - 1:
            return True

    return False


def is_prime(number: int, k: int) -> bool:
    """Probabilistic test of number for simplicity using the Miller-Rabin test.

    Args:
        number: is the number to be tested.
        k: number of tests. The larger the number, the less likely it is that a composite number
            will be misidentified as a prime number. (1/4)^k

    Returns:
        True if the number is probably prime else False

    """
    if number < 2 or number == 4:
        return False
    if number <= 3:
        return True

    d = number - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(1, k):
        if miller_rabin_test(d, number) is False:
            return False

    return True

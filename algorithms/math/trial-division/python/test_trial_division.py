import unittest
from math import isqrt

from is_prime import is_prime


class TrialDivisionTests(unittest.TestCase):
    def test_small_integers_against_unfiltered_division(self) -> None:
        for n in range(-10, 3000):
            expected = n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))
            self.assertEqual(is_prime(n), expected, n)

    def test_integer_square_root_and_divisors_at_the_boundary(self) -> None:
        self.assertFalse(is_prime(49))
        self.assertFalse(is_prime(121))
        self.assertFalse(is_prime(5 * (2**2048 + 3)))
        self.assertTrue(is_prime(997))

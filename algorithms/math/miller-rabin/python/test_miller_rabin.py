import unittest
from math import isqrt
from random import Random
from unittest.mock import patch

from is_prime import is_prime


class MillerRabinTests(unittest.TestCase):
    def test_one_round_actually_rejects_a_composite(self) -> None:
        with patch("is_prime.random.randrange", return_value=2) as choose_base:
            self.assertFalse(is_prime(9, 1))
        choose_base.assert_called_once_with(2, 8)

    def test_round_count_and_full_base_range(self) -> None:
        with patch("is_prime.random.randrange", return_value=9) as choose_base:
            self.assertTrue(is_prime(11, 5))
        self.assertEqual(choose_base.call_count, 5)
        choose_base.assert_called_with(2, 10)
        with self.assertRaises(ValueError):
            is_prime(17, 0)

    def test_seeded_rounds_against_trial_division(self) -> None:
        with patch("is_prime.random.randrange", side_effect=Random(42).randrange):
            for n in range(-4, 3000):
                expected = n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))
                self.assertEqual(is_prime(n, 12), expected, n)
            self.assertFalse(is_prime(561, 16))
            self.assertTrue(is_prime(2**61 - 1, 16))

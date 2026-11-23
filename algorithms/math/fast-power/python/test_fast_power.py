import unittest

from fast_power import fast_power


class FastPowerTests(unittest.TestCase):
    def test_integer_powers_and_reciprocals(self) -> None:
        for base in range(-5, 6):
            for exponent in range(-8, 9):
                if base or exponent >= 0:
                    self.assertEqual(fast_power(base, exponent), pow(base, exponent))
        self.assertEqual(fast_power(-1, -(2**63)), 1.0)

    def test_modular_power_including_inverses_and_zero_exponent(self) -> None:
        for base in range(-5, 6):
            for exponent in range(-6, 7):
                for modulus in range(-5, 6):
                    try:
                        expected = pow(base, exponent, modulus)
                    except ValueError:
                        with self.assertRaises(ValueError):
                            fast_power(base, exponent, modulus)
                    else:
                        self.assertEqual(fast_power(base, exponent, modulus), expected)

    def test_zero_to_negative_power(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            fast_power(0, -1)

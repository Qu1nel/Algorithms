import unittest
from dataclasses import dataclass, field
from unittest.mock import patch
from itertools import product

from quick_sort import quick_sort


class SortingTests(unittest.TestCase):
    def test_small_sequences_against_sorted(self) -> None:
        for size in range(6):
            for values in product(range(-1, 2), repeat=size):
                mutable = list(values)
                self.assertEqual(quick_sort(values), sorted(values))
                self.assertEqual(quick_sort(mutable), sorted(values))
                self.assertEqual(mutable, list(values))

    def test_non_list_sequence_and_negative_values(self) -> None:
        values = range(8, -9, -1)
        self.assertEqual(quick_sort(values), sorted(values))

    def test_equal_keys_keep_their_order(self) -> None:
        @dataclass(order=True)
        class Record:
            key: int
            label: str = field(compare=False)

        first, second = Record(2, "first"), Record(2, "second")
        low = Record(1, "low")
        result = quick_sort((first, low, second))
        self.assertIs(result[0], low)
        self.assertIs(result[1], first)
        self.assertIs(result[2], second)

    def test_repeated_extreme_pivots_do_not_exhaust_the_call_stack(self) -> None:
        values = list(range(1100))
        with patch("quick_sort.random.choice", side_effect=lambda values: values[0]):
            self.assertEqual(quick_sort(values), values)

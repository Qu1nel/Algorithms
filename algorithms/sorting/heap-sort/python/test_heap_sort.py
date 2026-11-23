import unittest
from itertools import product

from heap_sort import heap_sort


class SortingTests(unittest.TestCase):
    def test_small_sequences_against_sorted(self) -> None:
        for size in range(6):
            for values in product(range(-1, 2), repeat=size):
                mutable = list(values)
                self.assertEqual(heap_sort(values), sorted(values))
                self.assertEqual(heap_sort(mutable), sorted(values))
                self.assertEqual(mutable, list(values))

    def test_non_list_sequence_and_negative_values(self) -> None:
        values = range(8, -9, -1)
        self.assertEqual(heap_sort(values), sorted(values))

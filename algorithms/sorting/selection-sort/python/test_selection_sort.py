import unittest
from itertools import product

from selection_sort import selection_sort


class SortingTests(unittest.TestCase):
    def test_small_sequences_against_sorted(self) -> None:
        for size in range(6):
            for values in product(range(-1, 2), repeat=size):
                mutable = list(values)
                self.assertEqual(selection_sort(values), sorted(values))
                self.assertEqual(selection_sort(mutable), sorted(values))
                self.assertEqual(mutable, list(values))

    def test_non_list_sequence_and_negative_values(self) -> None:
        values = range(8, -9, -1)
        self.assertEqual(selection_sort(values), sorted(values))

    def test_comparison_count_on_sorted_and_reversed_inputs(self) -> None:
        for order in (range(8), range(7, -1, -1)):
            comparisons = 0

            class Key:
                def __init__(self, value: int) -> None:
                    self.value = value

                def __gt__(self, other: "Key") -> bool:
                    nonlocal comparisons
                    comparisons += 1
                    return self.value > other.value

            self.assertEqual([key.value for key in selection_sort([Key(i) for i in order])], list(range(8)))
            self.assertEqual(comparisons, 8 * 7 // 2)

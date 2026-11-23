import unittest
from itertools import combinations_with_replacement

from merge import merge, merge_sequence


class MergeTests(unittest.TestCase):
    def test_mixed_sequence_types(self) -> None:
        self.assertEqual(merge(range(-3, 5, 2), (-2, 0, 3)), [-3, -2, -1, 0, 1, 3, 3])
        self.assertEqual(merge((), [1, 2]), [1, 2])

    def test_small_inputs_against_sorted(self) -> None:
        sequences = [row for size in range(4) for row in combinations_with_replacement(range(3), size)]
        for a in sequences:
            for b in sequences:
                self.assertEqual(merge(a, b), sorted(a + b))

    def test_mutating_variant_leaves_unconsumed_suffix(self) -> None:
        a, b = [1, 3, 7], [2, 4]
        self.assertEqual(merge_sequence(a, b), [1, 2, 3, 4, 7])
        self.assertEqual(a, [7])
        self.assertEqual(b, [])

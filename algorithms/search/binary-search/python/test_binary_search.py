import unittest
from itertools import combinations_with_replacement

from binary_search import binary_search


class BinarySearchTests(unittest.TestCase):
    def test_rightmost_match_against_linear_search(self) -> None:
        for size in range(8):
            for items in combinations_with_replacement(range(-2, 3), size):
                for target in range(-3, 4):
                    expected = max((i for i, item in enumerate(items) if item == target), default=-1)
                    self.assertEqual(binary_search(items, target), expected)

    def test_boundary_and_duplicate_examples(self) -> None:
        self.assertEqual(binary_search([], 1), -1)
        self.assertEqual(binary_search([1], 1), 0)
        self.assertEqual(binary_search([1, 2, 2, 5], 2), 2)
        self.assertEqual(binary_search(range(20), 19), 19)

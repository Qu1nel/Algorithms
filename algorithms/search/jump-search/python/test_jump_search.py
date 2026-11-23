import unittest
from itertools import combinations_with_replacement

from jump_search import jump_search


class JumpSearchTests(unittest.TestCase):
    def test_membership_against_linear_search(self) -> None:
        for size in range(8):
            for items in combinations_with_replacement(range(-2, 3), size):
                for target in range(-3, 4):
                    index = jump_search(items, target)
                    if target in items:
                        self.assertGreaterEqual(index, 0)
                        self.assertLess(index, len(items))
                        self.assertEqual(items[index], target)
                    else:
                        self.assertEqual(index, -1)

    def test_duplicate_at_block_boundary_and_partial_final_block(self) -> None:
        self.assertEqual(jump_search([0, 1, 1, 1, 1], 1), 2)
        self.assertEqual(jump_search(range(15), 14), 14)

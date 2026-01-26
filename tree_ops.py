from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

BST : TypeAlias = Union[ 'BSTNode', None ]

@dataclass(frozen=True)
class BSTNode:
    value : Any
    left : BST
    right : BST

# Find the size of a given binary tree
def size(bst : BST) -> int:
    match bst:
        case None:
            return 0
        case BSTNode(_, left, right):
            return 1 + size(left) + size(right)

# Count num of leaf nodes within a BST
def num_leaf_nodes(bst : BST) -> int:
    match bst:
        case None:
            return 0
        case BSTNode(_, None, None):
            return 1
        case BSTNode(_, left, right):
            return num_leaf_nodes(left) + num_leaf_nodes(right)

# Sum up all the values within the BST
def sum(bst : BST) -> int:
    total = 0
    match bst:
        case None:
            return 0
        case BSTNode(value, left, right):
            total += value + sum(left) + sum(right)
    return total

# Determine the height of any given BST
def height(bst : BST) -> int:
    match bst:
        case None:
            return 0
        case BSTNode(_,left, right):
            if height(left) >= height(right):
                return 1 + height(left)
            else:
                return 1 + height(right)

# Check if a given BST has any triples
def has_triple(bst : BST, n : int) -> bool:
    match bst:
        case None:
            return False
        case BSTNode(value, left, right):
            if n == value:
                if left != None and left.value == 3 * n:
                    return True
                if right != None and right.value == 3 * n:
                    return True
    return has_triple(left, n) or has_triple(right, n)

# Subtract one from every value within a given BST
def sub_one_map(bst : BST) -> BST:
    match bst:
        case None:
            return None
        case BSTNode(value, left, right):
            new_bst = BSTNode(value - 1, sub_one_map(left), sub_one_map(right))
    return new_bst







class Tests(unittest.TestCase):
    bt_1: BST = BSTNode(4,
                            BSTNode(9,
                                   BSTNode(19, None, None),
                                   BSTNode(2, BSTNode(103, None, None), None)
                                   ),
                            BSTNode(42,
                                   None,
                                   BSTNode(7, None, None)))

    bt_2: BST = BSTNode(2,
                        BSTNode(6, None, None),
                        BSTNode(4, None,
                                BSTNode(9, None, None)))
    def test_size(self):
        self.assertEqual(size(self.bt_1), 7)
        self.assertEqual(size(self.bt_2), 4)

    def test_num_leaf_nodes(self):
        self.assertEqual(num_leaf_nodes(self.bt_1), 3)
        self.assertEqual(num_leaf_nodes(self.bt_2), 2)

    def test_sum(self):
        self.assertEqual(sum(self.bt_1), 186)
        self.assertEqual(sum(self.bt_2), 21)

    def test_height(self):
        self.assertEqual(height(self.bt_1), 4)
        self.assertEqual(height(self.bt_2), 3)

    def test_has_triple(self):
        self.assertEqual(has_triple(self.bt_1, 3), False)
        self.assertEqual(has_triple(self.bt_2, 2), True)

    def test_sub_one_map(self):
        self.assertEqual(sub_one_map(self.bt_1), BSTNode(3,
                            BSTNode(8,
                                   BSTNode(18, None, None),
                                   BSTNode(1, BSTNode(102, None, None), None)
                                   ),
                            BSTNode(41,
                                   None,
                                   BSTNode(6, None, None))))
        self.assertEqual(sub_one_map(self.bt_2), BSTNode(1,
                        BSTNode(5, None, None),
                        BSTNode(3, None,
                                BSTNode(8, None, None))))



# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
if __name__ == "__main__":
    unittest.main()

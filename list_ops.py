from typing import *
from dataclasses import dataclass
import unittest
import math
import sys

sys.setrecursionlimit(10**6)

IntList : TypeAlias = Union[None,'LLNode']

@dataclass(frozen=True)
class LLNode:
    value : int
    rest : IntList

# Find the length of a given linked list
def length(ll : IntList) -> int:
    match ll:
        case None:
            return 0
        case LLNode( _ , r ):
            return 1 + length(r)

# Add values within an IntList
def sum(ll : IntList) -> int:
    total = 0
    match ll:
        case None:
            return 0
        case LLNode( v , r):
            total += v + sum(r)
    return total

# Return the number of values greater than a given threshold value
def count_greater_than(ll : IntList, thresh : int) -> int:
    count = 0
    match ll:
        case None:
            return count
        case LLNode(v, r):
            if v >= thresh:
                count += 1
            count += count_greater_than(r, thresh)
    return count

# Provide index where given vlue is first found
def find(ll : IntList, val : int) -> int:
    index = 0
    match ll:
        case None:
            raise ValueError('No value found')
        case LLNode( v , r ):
            if v == val:
                return index
            else:
                index += 1
                find( r , val)
    return index

# Subtract one from each number of a linked list
def sub_one_map(ll : IntList) -> IntList:
    match ll:
        case None:
            return None
        case LLNode(v, r):
            new_ll = LLNode( v - 1 , sub_one_map(r))
            return new_ll

# Insert a value at any given index
def insert(ll : IntList, index : int, to_insert : int) -> IntList:
    match ll:
        case None:
            raise ValueError('index out of bounds')
        case LLNode(v, r):
            if index == 0:
                return LLNode(to_insert, ll)
            else:
                return LLNode(v, insert(r, index - 1, to_insert))

class Tests(unittest.TestCase):
    ll_0  = None
    ll_1 = LLNode(9, None)
    ll_2 = LLNode(9, LLNode(10, None))
    ll_3 = LLNode(9, LLNode(10, LLNode(11, None)))

    def test_length(self):
        self.assertEqual(length(self.ll_0), 0)
        self.assertEqual(length(self.ll_1), 1)
        self.assertEqual(length(self.ll_2), 2)
        self.assertEqual(length(self.ll_3), 3)
    def test_sum(self):
        self.assertEqual(sum(self.ll_0), 0)
        self.assertEqual(sum(self.ll_1), 9)
        self.assertEqual(sum(self.ll_2), 19)
        self.assertEqual(sum(self.ll_3), 30)
    def test_count_greater_than(self):
        self.assertEqual(count_greater_than(self.ll_0, 10), 0)
        self.assertEqual(count_greater_than(self.ll_1, 10), 0)
        self.assertEqual(count_greater_than(self.ll_2, 10), 1)
        self.assertEqual(count_greater_than(self.ll_3, 10), 2)
    def test_find(self):
        self.assertNotEqual(find(self.ll_1, 9), 1)
        self.assertNotEqual(find(self.ll_2, 10), 2)
        self.assertNotEqual(find(self.ll_3, 11), 3)
    def test_sub_one_map(self):
        self.assertEqual(sub_one_map(self.ll_1), LLNode(8, None))
        self.assertEqual(sub_one_map(self.ll_2), LLNode(8, LLNode(9, None)))
        self.assertEqual(sub_one_map(self.ll_3), LLNode(8, LLNode(9, LLNode(10, None))))

    def test_insert(self):
        self.assertEqual(insert(self.ll_1, 0, 10), LLNode(10, LLNode(9, None)))
        self.assertEqual(insert(self.ll_1, 0, 10), LLNode(10, LLNode(9, None)))
        self.assertEqual(insert(self.ll_1, 0, 10), LLNode(10, LLNode(9, None)))


# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
if __name__ == '__main__':
    unittest.main()

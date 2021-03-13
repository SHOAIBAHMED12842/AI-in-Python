import unittest
import random

# each assignment will be checked as std1
# don't change this line
from std1 import * 

class unit_test(unittest.TestCase):

    def test_1(self):
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        p = MaxPriorityHeap(data)
        self.assertTrue(p.Peek() == 12)

    def test_2(self):
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        p = MaxPriorityHeap(data)
        self.assertTrue(p.ExtractMaximum() == 12)
        self.assertTrue(p.ExtractMaximum() == 11)

    def test_3(self):
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        p = MaxPriorityHeap(data)
        self.assertTrue(p.Peek() == 12)
        p.HeapIncreaseKey(1, 100)
        self.assertTrue(p.Peek() == 100)

    def test_4(self):
        data = [1,3,4]
        p = MaxPriorityHeap(data)
        self.assertTrue(p.ExtractMaximum() == 4)
        self.assertTrue(p.ExtractMaximum() == 3)
        self.assertTrue(p.ExtractMaximum() == 1)


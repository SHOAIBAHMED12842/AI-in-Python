import unittest
import random

# each assignment will be checked as std1
# don't change this line
from std1 import * 

class unit_test(unittest.TestCase):

    # instance checking
    def test_1(self):
        n = Node(10)
        self.assertIsInstance(n, Node)
        b = BSTree()
        self.assertIsInstance(b, BSTree)
    
    # build and find checking
    def test_2(self):
        b = BSTree()
        b.Build([1,2,3,4,5])
        f = b.Find(5)
        self.assertTrue(f.value == 5)
        f = b.Find(6)
        self.assertTrue(f == None)
    
    # Insert and Find checking
    def test_3(self):
        b = BSTree()
        b.Insert(10)
        b.Insert(5)
        b.Insert(17)
        f = b.Find(10)
        self.assertTrue(f.value == 10)
        f = b.Find(5)
        self.assertTrue(f.value == 5)
        f = b.Find(17)
        self.assertTrue(f.value == 17)
    
    def CreateTree(self):
        b = BSTree()
        b.Insert(50)
        b.Insert(75)
        b.Insert(85)
        b.Insert(25)
        b.Insert(35)
        b.Insert(17)
        return(b)
    
    def test_4(self):
        b = self.CreateTree()
        f = b.Find(25)
        self.assertTrue(f.value == 25)
        self.assertTrue(f.left.value == 17)
        self.assertTrue(f.right.value == 35)
    
    # delete case 1
    def test_5(self):
        b = self.CreateTree()
        r = b.Delete(85)
        self.assertTrue(r)
        f = b.Find(85)
        self.assertTrue(f == None)
        f = b.Find(75)
        self.assertTrue(f.right == None)
        b.Insert(85)
        f = b.Find(85)
        self.assertTrue(f != None)
    
    # Delete case 2
    def test_6(self):
        b = self.CreateTree()
        r = b.Delete(75)
        self.assertTrue(r)
        f = b.Find(75)
        self.assertTrue(f == None)
        f = b.Find(50)
        self.assertTrue(f.right.value == 85)
    
    # delete case 3
    def test_7(self):
        b = self.CreateTree()
        b.Insert(30)
        r = b.Delete(25)
        self.assertTrue(r)
        f = b.Find(25)
        self.assertTrue(f == None)
        f = b.Find(50)
        self.assertTrue(f.left.value == 30)
    #height
    def test_8(self):
        b = self.CreateTree()
        b.Insert(30)
        self.assertTrue(b.Height() == 3)
        b = BSTree()
        b.Insert(50)
        self.assertTrue(b.Height() == 0)
    
    # GetUncle
    def test_9(self):
        b = self.CreateTree()
        b.Insert(30)
        u = b.GetUncle(17)
        self.assertTrue(u.value == 75)
        u = b.GetUncle(30)
        self.assertTrue(u.value == 17)
    
    # GetSibling    
    def test_10(self):
        b = self.CreateTree()
        b.Insert(30)
        s = b.GetSibling(17)
        self.assertTrue(s.value == 35)
        s = b.GetSibling(35)
        self.assertTrue(s.value == 17)
        s = b.GetSibling(85)
        self.assertTrue(s == None)
    
    # IsLeft / IsRight
    def test_11(self):
        b = self.CreateTree()
        self.assertTrue(b.IsLeft(25) == True)
        self.assertTrue(b.IsLeft(17) == True)
        self.assertTrue(b.IsRight(25) == False)
        self.assertTrue(b.IsRight(75) == True)
        self.assertTrue(b.IsRight(85) == True)
        
    # RotateLeft - simple
    def test_12(self):
        b = self.CreateTree()
        b.Insert(30)
        b.RotateLeft(25)
        f = b.Find(50)
        self.assertTrue(f != None)
        self.assertTrue(f.left != None)
        self.assertTrue(f.left.value == 35)
        self.assertTrue(f.left.right == None)
        self.assertTrue(f.left.left != None)
        self.assertTrue(f.left.left.value == 25)
        f = b.Find(25)
        self.assertTrue(f != None and f.right != None and f.right.value == 30)
    
    # Rotate Left complex
    def test_13(self):
        b = self.CreateTree()
        b.Insert(65)
        b.RotateLeft(50)
        f = b.Find(75)
        self.assertTrue(f != None and f.left != None and f.right != None)
        self.assertTrue(f.value == 75 and f.left.value == 50 and f.right.value == 85)
        self.assertTrue(f.left.right != None and f.left.right.value == 65)
        
    
    # rotate right - simple
    def test_14(self):
        b = self.CreateTree()
        b.Insert(10)
        b.Insert(21)
        b.RotateRight(25)
        f = b.Find(50)
        self.assertTrue(f != None and f.left != None and f.left.value == 17)
        f = f.left
        self.assertTrue(f.right != None and f.right.value == 25)
        self.assertTrue(f.right.left != None and f.right.left.value == 21)
        self.assertTrue(f.left != None and f.left.value == 10)
     
  
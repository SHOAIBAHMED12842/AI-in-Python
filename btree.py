# CS322 : Design and Analysis of Algorithms
# Assignment 4
# Implement the functions given in the BSTree class in order to implement an extenedd BST.
# Due Date: 28 July 2020

#Instructions:
# Do not change the function name
# You can add more functions if required
# Your file name must be your Roll Number
# Uncompilable file will not be graded
# Plagiarism will not be tolerated at all
# Assignment will be checked through automatic process

# class to represent a node in the tree
class Node:
    def __init__(self, value = None):
        # 0 = Red, 1 = Black
        self.color = 0
        # value of the node
        self.value = value
        # left child
        self.left = None
        # right child
        self.right = None

# To represent and extended BST
class BSTree:

    # constructor
    # you can add more lines if requried
    def __init__(self):
        self.root = None

    # Insert an element in the tree as per BST rules (duplicates are ignored)
    def Insert(self, value):
        pass

    """
    Find an element in the tree with value 'value'.
    Returns the node if found, otherwise returns None
    """
    def Find(self, value) -> Node: 
        pass
    """
    Delete the element from the tree (as per BST)
    """
    def Delete(self, value) -> bool:
        pass

    # Rotate left at the node with value 'v'
    def RotateLeft(self, v):
        pass

    # Rotate right at the node with value 'v'
    def RotateRight(self, value):
        pass

    # returns the height of the tree
    def Height(self):
        pass

    # returns the Uncle node i.e. another child of the parent's parent
    # returns Node if the element found in the tree, otherwise returns None
    def GetUncle(self, v):
        pass

    # returns the Sibling node i.e. another child of the parent
    # returns Node if the element found in the tree, otherwise returns None
    def GetSibling(self, value):
        pass

    # Returns true if the node with value v is a left child of its parent
    # otherwise returns False
    def IsLeft(self, value) -> bool:
        pass

    # Returns true if the node with value v is a right child of its parent,
    # otherwise returns False
    def IsRight(self, value) -> bool:
        pass

    # Create a BST for the items given in the 'data'
    def Build(self, data: list):
        pass

    
def Test_BSTree():
    t = BSTree()
    t.Build([5,6,3,1,2,4])
    

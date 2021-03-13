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
        # parent
        self.parent = None

# To represent and extended BST
class BSTree:

    # constructor
    # you can add more lines if requried
    def __init__(self):
        self.root = None

    # Insert an element in the tree as per BST rules (duplicates are ignored)
    def Insert(self, value):
        self.root = self.InsertHelper(value, self.root)

    def InsertHelper(self, value, node):

        if node == None:# adding at root
            n = Node(value)
            n.parent = None
            return(n)
        elif node.value == value:
            return(node)
        elif value < node.value: # adding at left node
            if node.left == None:
                node.left = Node(value)
                node.left.parent = node
            else: # left node is not empty
                node.left = self.InsertHelper(value, node.left)
            return(node)
        else:
            if node.right == None: # adding at right node
                node.right = Node(value)
                node.right.parent = node
            else: # right node is not empty
                node.right = self.InsertHelper(value,node.right)
            return(node)
            

    """
    Find an element in the tree with value 'value'.
    Returns the node if found, otherwise returns None
    """
    def Find(self, value) -> Node:
        return self.FindHelper(value, self.root)

    def FindHelper(self, value, node):

        if node == None:
            return None
        elif node.value == value:
            return node
        elif value < node.value:
            return self.FindHelper(value, node.left)
        else:
            return self.FindHelper(value, node.right)

    # return minimum node
    def FindMin(self, node):
        if node == None:
            return None

        if node.left == None:
            return node
        else:
            return self.FindMin(node.left)
        
        
    """
    Delete the element from the tree (as per BST)
    """
    def Delete(self, value) -> bool:
        # find node
        f = self.Find(value)
        return self.DeleteHelper(f)

    # handle as a node
    def DeleteHelper(self, f):   
        if f == None: # not found
            return(False)
        
        # case 1
        if self.IsLeaf(f):
            if self.IsLeftHelper(f):
                f.parent.left = None
            else:
                f.parent.right = None

            return(True) #success
        # case 2
        elif f.left == None: # right child has a node
            if self.IsLeftHelper(f):
                f.parent.left = f.right
            else:
                f.parent.right = f.right

            return(True) #success
        elif f.right == None: # left child has a ndoe
            if self.IsLeftHelper(f):
                f.parent.left = f.left
            else:
                f.parent.right = f.left

            return(True) #success
        # case 3
        else: 
            suc = self.FindMin(f.right)
            f.value = suc.value
            return self.DeleteHelper(suc)

        return(False) #shouldn't reach here

        
    # Rotate left at the node with value 'v'
    def RotateLeft(self, v):
        f = self.Find(v)

        if f == None:
            return
        elif f.right == None:
            return

        x = f
        z = x.right
        if x.right is not None:
            gamma = x.right.left
        else:
            gamma = None

        z.left = x
        x.right = gamma

        if self.IsLeftHelper(x):
            if x.parent is not None:
                x.parent.left = z
        else:
            if x.parent is not None:
                x.parent.right = z
        
        z.parent = x.parent
        x.parent = z

        if z.parent is None:
            self.root = z


    # Rotate right at the node with value 'v'
    def RotateRight(self, value):
        f = self.Find(value)

        if f == None:
            return
        elif f.left == None:
            return

        x = f
        y = x.left
        beta = x.left.right

        y.right  = x
        x.left =beta

        if self.IsLeftHelper(f):
            if x.parent is not None:
                x.parent.left = y
        else:
            if x.parent is not None:
                x.parent.right = y

        y.parent = x.parent
        x.parent = y

        if y.parent is None:
            self.root = y
            
        

    # returns the height of the tree
    def Height(self):
        if self.root == None:
            return 0
        else:
            return self.HeightHelper(self.root)

    def HeightHelper(self, node):
        if node == None:
            return -1

        return 1+max(self.HeightHelper(node.left),self.HeightHelper(node.right))

        
    # returns the Uncle node i.e. another child of the parent's parent
    # returns Node if the element found in the tree, otherwise returns None
    def GetUncle(self, v):
        f = self.Find(v)

        if f is not None and f.parent is not None and f.parent.parent is not None:
            if self.IsLeftHelper(f.parent):
                return(f.parent.parent.right)
            else:
                return(f.parent.parent.left)

        return(None)

    # returns the Sibling node i.e. another child of the parent
    # returns Node if the element found in the tree, otherwise returns None
    def GetSibling(self, value):
        f = self.Find(value)

        if f is not None and f.parent is not None:
            if self.IsLeftHelper(f):
                return(f.parent.right)
            else:
                return(f.parent.left)

        return(None)

    # Returns true if the node with value v is a left child of its parent
    # otherwise returns False
    def IsLeft(self, value) -> bool:
        f = self.Find(value)
        return(self.IsLeftHelper(f))

    def IsLeftHelper(self, node):
        if node == None:
            return(False)

        if node.parent == None:
            return(False)

        return(node.parent.left != None and node.parent.left.value == node.value)

    # Returns true if the node with value v is a right child of its parent,
    # otherwise returns False
    def IsRight(self, value) -> bool:
        f = self.Find(value)
        return(self.IsRightHelper(f))
        

    def IsRightHelper(self, node):
        if node == None:
            return(False)

        if node.parent == None:
            return(False)

        return(node.parent.right != None and node.parent.right.value == node.value)

    def IsLeaf(self, node):
        if node == None:
            return(False)
        if node.left == None and node.right == None:
            return(True)

        return(False)

    # Create a BST for the items given in the 'data'
    def Build(self, data: list):
        self.root = None
        for x in data:
            self.Insert(x)
        

    
def Test_BSTree():
    t = BSTree()
    t.Build([5,16,3,1,2,4,8,20])
    return(t)

t = Test_BSTree()

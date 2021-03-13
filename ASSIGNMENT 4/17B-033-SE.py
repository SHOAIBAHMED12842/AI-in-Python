#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
import sys

# class to represent a no in the tree
class Node:
    def __init__(self, value = None):
        # 0 = Red, 1 = Black
        self.color = 1
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
        self.NILLL = Node(0)
        self.NILLL.color = 0
        self.NILLL.left = None
        self.NILLL.right = None
        self.root = self.NILLL
        #self.root = None
        
    def preorder(self):
        self.pre_order(self.root)

    def inorder(self):
        self.in_order(self.root)

    def postorder(self):
        self.post_order(self.root)
        
    # Preorder
    def pre_order(self, no):
        if no != NILLL:
            sys.stdout.write(no.value + " ")
            self.pre_order(no.left)
            self.pre_order(no.right)

    # Inorder
    def in_order(self, no):
        if no != NILLL:
            self.in_order(no.left)
            sys.stdout.write(no.value + " ")
            self.in_order(no.right)

    # Postorder
    def post_order(self, no):
        if no != NILLL:
            self.post_order(no.left)
            self.post_order(no.right)
            sys.stdout.write(no.value + " ")
            
            
    def minimum(self, no):
        while no.left != self.NILLL:
            no = no.left
        return no

    def maximum(self, no):
        while no.right != self.NILLL:
            no = no.right
        return no

    def successor(self, x):
        if x.right != self.NILLL:
            return self.minimum(x.right)

        t = x.parent
        while t != self.NILLL and x == t.right:
            x = t
            t = t.parent
        return t

    def predecessor(self,  x):
        if (x.left != self.NILLL):
            return self.maximum(x.left)

        t = x.parent
        while t != self.NILLL and x == t.left:
            x = t
            t = t.parent

        return t

    
    # Insert an element in the tree as per BST rules (duplicates are ignored)
    def Insert(self, value):
        no = Node(value)    
        no.parent = None
        no.value = value
        no.left = self.NILLL
        no.right = self.NILLL
        no.color = 1

        t = None
        s = self.root

        while s != self.NILLL:
            t = s
            if no.value < s.value:
                s = s.left
            else:
                s = s.right

        no.parent = t
        if t == None:
            self.root = no
        elif no.value < t.value:
            t.left = no
        else:
            t.right = no

        if no.parent == None:
            no.color = 0
            return

        if no.parent.parent == None:
            return

        self.finins(no)
        pass
    
    # Balance tree after insertion
    def finins(self, value):
        while value.parent.color == 1:
            if value.parent == value.parent.parent.right:
                u = value.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    value.parent.color = 0
                    value.parent.parent.color = 1
                    value = value.parent.parent
                else:
                    if value == value.parent.left:
                        value = value.parent
                        self.RotateRight(value)
                    value.parent.color = 0
                    value.parent.parent.color = 1
                    self.RotateLeft(value.parent.parent)
            else:
                u = value.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    value.parent.color = 0
                    value.parent.parent.color = 1
                    value = value.parent.parent
                else:
                    if value == value.parent.right:
                        value = value.parent
                        self.RotateLeft(value)
                    value.parent.color = 0
                    value.parent.parent.color = 1
                    self.RotateRight(value.parent.parent)
            if value == self.root:
                break
        self.root.color = 0


    #"""
    #Find an element in the tree with value 'value'.
    #Returns the no if found, otherwise returns None
    #"""
    
    def Find(self, value): #-> Node: 
        return self.Tfind(self.root, value)
        pass
    #"""
    def Tfind(self,no, value):
        
        if no is None or value == no.value:
            return no

        if value < no.value:
            return self.Tfind(no.left, value)
        return self.Tfind(no.right, value)
        
    # r get
    def Rget(self):
        return self.root
    
    #Delete the element from the tree (as per BST)
    #"""
    def Delete(self, value):#-> bool:
        self.Ndel(self.root, value)
        pass
    
    # No deletion
    def Ndel(self, no, value):
        v = self.NILLL
        while no != self.NILLL:
            if no.value == value:
                v = no

            if no.value <= value:
                no = no.right
            else:
                no = no.left

        if v == self.NILLL:
            print("Cannot find value in the tree")
            return

        t = v
        t_original_c = t.color
        if v.left == self.NILLL:
            s = v.right
            self.transroot(v, v.right)
        elif (v.right == self.NILLL):
            s = v.left
            self.transroot(v, v.left)
        else:
            t = self.minimum(v.right)
            t_original_c = t.color
            s = t.right
            if t.parent == v:
                s.parent = t
            else:
                self.transroot(t, t.right)
                t.right = v.right
                t.right.parent = t

            self.transroot(v, t)
            t.left = v.left
            t.left.parent = t
            t.color = v.color
        if t_original_c == 0:
            self.fixdel(s)
    
    # Balancing the tree after deletion
    def fixdel(self, h):
        while h != self.root and h.color == 0:
            if h == h.parent.left:
                s = h.parent.right
                if s.color == 1:
                    s.color = 0
                    h.parent.color = 1
                    self.RotateLeft(h.parent)
                    s = h.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    h = h.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.RotateRight(s)
                        s = h.parent.right

                    s.color = h.parent.color
                    h.parent.color = 0
                    s.right.color = 0
                    self.RotateLeft(h.parent)
                    h = self.root
            else:
                s = h.parent.left
                if s.color == 1:
                    s.color = 0
                    h.parent.color = 1
                    self.RotateRight(h.parent)
                    s = h.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    h = h.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.RotateLeft(s)
                        s = h.parent.left

                    s.color = h.parent.color
                    h.parent.color = 0
                    s.left.color = 0
                    self.RotateRight(h.parent)
                    h = self.root
        h.color = 0

        
    def transroot(self, s, t):
        if s.parent == None:
            self.root = t
        elif s == s.parent.left:
            s.parent.left = t
        else:
            s.parent.right = t
        t.parent = s.parent

    
    
    # Rotate left at the node with value 'v'
    def RotateLeft(self, v):
        t = v.right
        v.right = t.left
        if t.left != self.NILLL:
            t.left.parent = v

        t.parent = v.parent
        if v.parent == None:
            self.root = t
        elif v == v.parent.left:
            v.parent.left = t
        else:
            v.parent.right = t
        t.left = v
        v.parent = t
        pass


    # Rotate right at the node with value 'v'
    def RotateRight(self, value):
        t = value.left
        value.left = t.right
        if t.right != self.NILLL:
            t.right.parent = value

        t.parent = value.parent
        if value.parent == None:
            self.root = t
        elif value == value.parent.right:
            value.parent.right = t
        else:
            value.parent.left = t
        t.right = value
        value.parent = t
        pass


    # returns the height of the tree
    def Height(self):
        return self.Rheight(self.root)
        pass
    
    def Rheight(self, no): 
        
        if no is None:
            return 0  
        else:
            return 1 + max(self.Rheight(no.left),self.Rheight(no.right))
        
    # returns the Uncle node i.e. another child of the parent's parent
    # returns Node if the element found in the tree, otherwise returns None
    def GetUncle(self, v):
        return self.guncle(self.root, v)
        pass
    
    def guncle(self,node,value):
        
        if node is None or value == node.value:
            return node
        elif (node.left.left != None and node.left.left.value == value):
            return node.right.right
    
        elif (node.right.right != None and node.right.right.value == value):
            return node.left.left
        else:
            return None
    # returns the Sibling node i.e. another child of the parent
    # returns Node if the element found in the tree, otherwise returns None
    def GetSibling(self, value):
        return self.gsibling(self.root, value)
        pass
    
    def gsibling(self,node,value):
        
        if node is None or value == node.value:
            return node
        elif (node.left != None and node.left.value == value):
            return node.right
    
        elif (node.right != None and node.right.value == value):
            return node.left
        else:
            return None
        
    # Returns true if the node with value v is a left child of its parent
    # otherwise returns False
    def IsLeft(self, value): #-> bool:
        return self.checkleft(self.root, value)
        pass
    
    def checkleft(self,node,value):
        if node is None or value == node.value:
            return node
        elif (node.left.parent != None and node.left.value == value):
            return True
        else:
            return False
    # Returns true if the node with value v is a right child of its parent,
    # otherwise returns False
    def IsRight(self, value): #-> bool:
        return self.checkleft(self.root, value)
        pass
    
    def checkright(self,node,value):
        if node is None or value == node.value:
            return node
        elif (node.right.parent != None and node.right.value == value):
            return True
        else:
            return False
    # Create a BST for the items given in the 'data'
    def Build(self, data: list):
        n=len(data)
        for i in range(n):
            self.Insert(data[i])
        pass
 
    # Printing the tree
    def printing1(self, no, ind, la):
        if no != self.NILLL:
            sys.stdout.write(ind)
            if la:
                sys.stdout.write("R----")
                ind += "     "
            else:
                sys.stdout.write("L----")
                ind += "|    "

            s_c = "RED" if no.color == 1 else "BLACK"
            print(str(no.value) + "(" + s_c + ")")
            self.printing1(no.left, ind, False)
            self.printing1(no.right, ind, True)
    
    def treeprint(self):
        self.printing1(self.root, "", True)
        
        
        
def Test_BSTree():
    t = BSTree()
    t.Build([5,6,3,1,2,4])
    
    


# In[ ]:





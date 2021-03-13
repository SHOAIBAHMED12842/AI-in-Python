#!/usr/bin/env python
# coding: utf-8

# In[6]:


# CS322 : Design and Analysis of Algorithms
# Bonus Assignment - (Max Points: 5)
# Implement the Maximum Priority Queue
# Refer Section 6.5 of the text book to learn about Priority Queue
# Due Date: 20 July 2020

#Instructions:
# Do not change the function name
# You can add more functions if require
# Your file name must be your Roll Number
# Uncompilable file will not be graded
# Plagiarism will not be tolerated at all


### ROLL NUMBER: <17B-033-SE>

class MaxPriorityHeap:
    
    sizeh = 0
    INF = 100000
    def __init__(self, data: list):
        # initialize the heap for given data
        self.data = data
        pass
    
    def BuildHeap(self, data: list):
        # build heap for the self.data
        self.data = data
        for i in range(sizeh//2, 0, -1):  
            MaxHeapify(data, i)
        pass

    def MaxHeapify(self,data: list, i: int):
        # perform max heapify
        self.data = data
        leftindex = leftchild(data, i)
        rightindex = rightchild(data, i)
        largest = i
        if ((leftindex <= sizeh) and (leftindex>0)):
            if (data[leftindex] > data[largest]):
                largest = leftindex

        if ((rightindex <= sizeh and (rightindex>0))):
            if (data[rightindex] > data[largest]):
                largest = rightindex
 
        if(largest != index):
            data[i], data[largest] = ddata[largest], data[i]
            MaxHeapify(data, largest)
        pass

    def HeapIncreaseKey(self,data: list, i:int , key: int):
        # increse the value of element i to the new value k
        self.data = data
        if(key<data[i]):
            print("New key is smaller than current key")
        data[i] = key
        while((i>1) and (data[parent(data, i)] < data[i])):
            data[i], data[parent(data, i)] = data[parent(data, i)], data[i]
            i = parent(data, i)
        pass
    
    def decrease_key(self,data: list, i:int , key: int):
        self.data = data
        data[i] = key
        MaxHeapify(data, i)
        pass
        
        
    def Peek(self,data: list):
        # retruns the maximum element
        self.data = data
        return data[1]
        pass
    
    def insert(self,data: list, i:int , key: int):
        self.data = data
        global sizeh
        sizeh = sizeh+1
        data[sizeh] = -1*INF
        HeapIncreaseKey(data, sizeh, key)

    def ExtractMaximum(self,data: list):
        # returns and remove the maximum element
        self.data = data
        global sizeh
        if (sizeh<1):
            print("Heap underflow")
        maxi = data[1]
        data[1] = data[sizeh]
        sizeh = sizeh-1
        MaxHeapify(data, 1)
        return maxi
        pass
    
    def rightchild(self,data: list, i: int):
        self.data = data
        if((((2*i)+1) < len(data)) and (i >= 1)):   
            return (2*i)+1
            return -1
        pass

    def leftchild(self,data: list, i: int):
        self.data = data
        if(((2*i) < len(data)) and (i >= 1)):
            return 2*i
            return -1
        pass
  
    def parent(self,data: list, i: int):
        self.data = data
        if ((i > 1) and (i < len(data))):
            return i//2
            return -1
        pass


# In[ ]:





# In[ ]:





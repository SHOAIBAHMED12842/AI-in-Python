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


### ROLL NUMBER: <provide your roll number>

class MaxPriorityHeap:
    
    def __init__(self, data: list):
        # initialize the heap for given data
        self.data = data
        pass
    
    def BuildHeap(self):
        # build heap for the self.data
        pass

    def MaxHeapify(self, i: int):
        # perform max heapify
        pass

    def HeapIncreaseKey(self, i:int , key: int):
        # increse the value of element i to the new value k
        pass

    def Peek(self):
        # retruns the maximum element
        pass

    def ExtractMaximum(self):
        # returns and remove the maximum element
        pass

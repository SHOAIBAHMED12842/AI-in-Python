#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plotgraph
import time
import sys



def main():
    sys.setrecursionlimit(50000)
    print("Welcome!\n1. Open\n2. High\n3. Low\n4. Close")
    print("Enter your choice :")
    dataset=pd.read_csv("data.csv")
    choose=int(input())
    if  choose==1:
        print("OPEN DATA")
        TIMEINSERTION = []
        TIMEQUICKSORT = []
        TIMEMERGESORT = []
        SIZEI=[]
        SIZEQ=[]
        SIZEM=[]
#-----------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
#----------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
#--------------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
#-----------------------------------------------------------------------------
        sizei=np.reshape(SIZEI, (13,1))
        sizeq=np.reshape(SIZEQ, (13,1))
        sizem=np.reshape(SIZEM, (13,1))
        #----------------------------------------------------
        timeinsertion=np.reshape(TIMEINSERTION, (13,1))
        timequicksort=np.reshape(TIMEQUICKSORT, (13,1))
        timemergesort=np.reshape(TIMEMERGESORT, (13,1))
        #---------------------------------------------------------------
        plotgraph.figure(figsize=(8,5))
        plotgraph.title('Time Complexity Insertion Sort vs Quick Sort vs Merge Sort', fontdict={'fontweight':'bold', 'fontsize': 18})
        plotgraph.plot(sizei, timeinsertion, color='blue', label='INSERTION')
        plotgraph.plot(sizeq, timequicksort, color='yellow', label='QUICK')
        plotgraph.plot(sizem, timemergesort, color='green',label='MERGE')
        #----------------------------------------------------------------
        plotgraph.xlabel('N')
        plotgraph.ylabel('Time (s)')
        plotgraph.legend()
        plotgraph.savefig('graph.png', dpi=300)
        print("Have a nice day!")
#---------------------------------------------------------------------
    elif(choose==2):
        print("HIGH DATA")
        TIMEINSERTION = []
        TIMEQUICKSORT = []
        TIMEMERGESORT = []
        SIZEI=[]
        SIZEQ=[]
        SIZEM=[]
#-----------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
#----------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
#--------------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
#-----------------------------------------------------------------------------
        sizei=np.reshape(SIZEI, (13,1))
        sizeq=np.reshape(SIZEQ, (13,1))
        sizem=np.reshape(SIZEM, (13,1))
        #----------------------------------------------------
        timeinsertion=np.reshape(TIMEINSERTION, (13,1))
        timequicksort=np.reshape(TIMEQUICKSORT, (13,1))
        timemergesort=np.reshape(TIMEMERGESORT, (13,1))
        #---------------------------------------------------------------
        plotgraph.figure(figsize=(8,5))
        plotgraph.title('Time Complexity Insertion Sort vs Quick Sort vs Merge Sort', fontdict={'fontweight':'bold', 'fontsize': 18})
        plotgraph.plot(sizei, timeinsertion, color='blue', label='INSERTION')
        plotgraph.plot(sizeq, timequicksort, color='yellow', label='QUICK')
        plotgraph.plot(sizem, timemergesort, color='green',label='MERGE')
        #----------------------------------------------------------------
        plotgraph.xlabel('N')
        plotgraph.ylabel('Time (s)')
        plotgraph.legend()
        plotgraph.savefig('graph.png', dpi=300)
        print("Have a nice day!")
#---------------------------------------------------------------------
    elif(choose==3):
        print("LOW DATA")
        TIMEINSERTION = []
        TIMEQUICKSORT = []
        TIMEMERGESORT = []
        SIZEI=[]
        SIZEQ=[]
        SIZEM=[]
#-----------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
#----------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
#--------------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
#-----------------------------------------------------------------------------
        sizei=np.reshape(SIZEI, (13,1))
        sizeq=np.reshape(SIZEQ, (13,1))
        sizem=np.reshape(SIZEM, (13,1))
        #----------------------------------------------------
        timeinsertion=np.reshape(TIMEINSERTION, (13,1))
        timequicksort=np.reshape(TIMEQUICKSORT, (13,1))
        timemergesort=np.reshape(TIMEMERGESORT, (13,1))
        #---------------------------------------------------------------
        plotgraph.figure(figsize=(8,5))
        plotgraph.title('Time Complexity Insertion Sort vs Quick Sort vs Merge Sort', fontdict={'fontweight':'bold', 'fontsize': 18})
        plotgraph.plot(sizei, timeinsertion, color='blue', label='INSERTION')
        plotgraph.plot(sizeq, timequicksort, color='yellow', label='QUICK')
        plotgraph.plot(sizem, timemergesort, color='green',label='MERGE')
        #----------------------------------------------------------------
        plotgraph.xlabel('N')
        plotgraph.ylabel('Time (s)')
        plotgraph.legend()
        plotgraph.savefig('graph.png', dpi=300)
        print("Have a nice day!")
#---------------------------------------------------------------------
    elif(choose==4):
        print("CLOSE DATA")
        TIMEINSERTION = []
        TIMEQUICKSORT = []
        TIMEMERGESORT = []
        SIZEI=[]
        SIZEQ=[]
        SIZEM=[]
#-----------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMEINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
#----------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMEQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
#--------------------------------------------------------------------------------------
        arraydata= dataset[:1].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:100].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:1000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:5000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:10000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:15000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:20000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:25000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:30000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:35000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:40000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:45000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        arraydata= dataset[:50000].values
        values=arraydata[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMEMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
#-----------------------------------------------------------------------------
        sizei=np.reshape(SIZEI, (13,1))
        sizeq=np.reshape(SIZEQ, (13,1))
        sizem=np.reshape(SIZEM, (13,1))
        #----------------------------------------------------
        timeinsertion=np.reshape(TIMEINSERTION, (13,1))
        timequicksort=np.reshape(TIMEQUICKSORT, (13,1))
        timemergesort=np.reshape(TIMEMERGESORT, (13,1))
        #---------------------------------------------------------------
        plotgraph.figure(figsize=(8,5))
        plotgraph.title('Time Complexity Insertion Sort vs Quick Sort vs Merge Sort', fontdict={'fontweight':'bold', 'fontsize': 18})
        plotgraph.plot(sizei, timeinsertion, color='blue', label='INSERTION')
        plotgraph.plot(sizeq, timequicksort, color='yellow', label='QUICK')
        plotgraph.plot(sizem, timemergesort, color='green',label='MERGE')
        #----------------------------------------------------------------
        plotgraph.xlabel('N')
        plotgraph.ylabel('Time (s)')
        plotgraph.legend()
        plotgraph.savefig('graph.png', dpi=300)
        print("Have a nice day!")
#---------------------------------------------------------------------
    else:
        print("INVALID INPUT")
#-----------------------------------insertionsort-------------------------------
def insertionSort(arr): 

    for i in range(1, len(arr)):
        keye = arr[i] 
        j = i-1
        while j >= 0 and keye < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = keye 
#-----------------------quicksort-----------------------------    
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
    
def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]     
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

#------------------------mergesort--------------------------------------   
def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
        
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
   
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
   
    i = 0      
    j = 0     
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  

    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

#-----------------------------------------------------------------------------------------        
            
if __name__ == "__main__":
    main()


# In[ ]:





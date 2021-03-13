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
        print("INSERTION SORT")
        TIMMERINSERTION = []
        TIMMERQUICKSORT = []
        TIMMERMERGESORT = []
        SIZEI=[]
        SIZEQ=[]
        SIZEM=[]
#-----------------------------------------------------------------------------------
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
#----------------------------------------------------------------------------------
        print("QUICK SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
#--------------------------------------------------------------------------------------
        print("MERGE SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,2]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
#-----------------------------------------------------------------------------
        sizei=np.reshape(SIZEI, (13,1))
        sizeq=np.reshape(SIZEQ, (13,1))
        sizem=np.reshape(SIZEM, (13,1))
        #----------------------------------------------------
        TIMMERINSERTION=np.reshape(TIMMERINSERTION, (13,1))
        TIMMERQUICKSORT=np.reshape(TIMMERQUICKSORT, (13,1))
        TIMMERMERGESORT=np.reshape(TIMMERMERGESORT, (13,1))
        #---------------------------------------------------------------
        plotgraph.figure(figsize=(8,5))
        plotgraph.title('Time Complexity Insertion Sort vs Quick Sort vs Merge Sort', fontdict={'fontweight':'bold', 'fontsize': 18})
        plotgraph.plot(sizei, TIMMERINSERTION, color='blue', label='INSERTION')
        plotgraph.plot(sizeq, TIMMERQUICKSORT, color='yellow', label='QUICK')
        plotgraph.plot(sizem, TIMMERMERGESORT, color='green',label='MERGE')
        #----------------------------------------------------------------
        plotgraph.xlabel('N')
        plotgraph.ylabel('Time (s)')
        plotgraph.legend()
        plotgraph.savefig('graph.png', dpi=300)
        print("Have a nice day!")
#---------------------------------------------------------------------
    elif(choose==2):
        print("HIGH DATA")
        TIMMERINSERTION = []
        TIMMERQUICKSORT = []
        TIMMERMERGESORT = []
        SIZEI=[]
        SIZEQ=[]
        SIZEM=[]
#-----------------------------------------------------------------------------------
        print("INSERTION SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
#----------------------------------------------------------------------------------
        print("QUICK SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
#--------------------------------------------------------------------------------------
        print("MERGE SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,3]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
#-----------------------------------------------------------------------------
        sizei=np.reshape(SIZEI, (13,1))
        sizeq=np.reshape(SIZEQ, (13,1))
        sizem=np.reshape(SIZEM, (13,1))
        #----------------------------------------------------
        TIMMERINSERTION=np.reshape(TIMMERINSERTION, (13,1))
        TIMMERQUICKSORT=np.reshape(TIMMERQUICKSORT, (13,1))
        TIMMERMERGESORT=np.reshape(TIMMERMERGESORT, (13,1))
        #---------------------------------------------------------------
        plotgraph.figure(figsize=(8,5))
        plotgraph.title('Time Complexity Insertion Sort vs Quick Sort vs Merge Sort', fontdict={'fontweight':'bold', 'fontsize': 18})
        plotgraph.plot(sizei, TIMMERINSERTION, color='blue', label='INSERTION')
        plotgraph.plot(sizeq, TIMMERQUICKSORT, color='yellow', label='QUICK')
        plotgraph.plot(sizem, TIMMERMERGESORT, color='green',label='MERGE')
        #----------------------------------------------------------------
        plotgraph.xlabel('N')
        plotgraph.ylabel('Time (s)')
        plotgraph.legend()
        plotgraph.savefig('graph.png', dpi=300)
        print("Have a nice day!")
#---------------------------------------------------------------------
    elif(choose==3):
        print("LOW DATA")
        TIMMERINSERTION = []
        TIMMERQUICKSORT = []
        TIMMERMERGESORT = []
        SIZEI=[]
        SIZEQ=[]
        SIZEM=[]
#-----------------------------------------------------------------------------------
        print("INSERTION SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
#----------------------------------------------------------------------------------
        print("QUICK SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
#--------------------------------------------------------------------------------------
        print("MERGE SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,4]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
#-----------------------------------------------------------------------------
        sizei=np.reshape(SIZEI, (13,1))
        sizeq=np.reshape(SIZEQ, (13,1))
        sizem=np.reshape(SIZEM, (13,1))
        #----------------------------------------------------
        TIMMERINSERTION=np.reshape(TIMMERINSERTION, (13,1))
        TIMMERQUICKSORT=np.reshape(TIMMERQUICKSORT, (13,1))
        TIMMERMERGESORT=np.reshape(TIMMERMERGESORT, (13,1))
        #---------------------------------------------------------------
        plotgraph.figure(figsize=(8,5))
        plotgraph.title('Time Complexity Insertion Sort vs Quick Sort vs Merge Sort', fontdict={'fontweight':'bold', 'fontsize': 18})
        plotgraph.plot(sizei, TIMMERINSERTION, color='blue', label='INSERTION')
        plotgraph.plot(sizeq, TIMMERQUICKSORT, color='yellow', label='QUICK')
        plotgraph.plot(sizem, TIMMERMERGESORT, color='green',label='MERGE')
        #----------------------------------------------------------------
        plotgraph.xlabel('N')
        plotgraph.ylabel('Time (s)')
        plotgraph.legend()
        plotgraph.savefig('graph.png', dpi=300)
        print("Have a nice day!")
#---------------------------------------------------------------------
    elif(choose==4):
        print("CLOSE DATA")
        TIMMERINSERTION = []
        TIMMERQUICKSORT = []
        TIMMERMERGESORT = []
        SIZEI=[]
        SIZEQ=[]
        SIZEM=[]
#-----------------------------------------------------------------------------------
        print("INSERTION SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        insertionSort(values) 
        end2_time = time.time()
        TIMMERINSERTION.append(end2_time-start2_time)
        SIZEI.append(n)
        print("Done values: ",n)
#----------------------------------------------------------------------------------
        print("QUICK SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1)
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        quickSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERQUICKSORT.append(end2_time-start2_time)
        SIZEQ.append(n)
        print("Done values: ",n)
#--------------------------------------------------------------------------------------
        print("MERGE SORT")
        dataset_vieay_view= dataset[:1].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:100].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:1000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:5000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:10000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:15000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:20000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:25000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:30000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:35000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:40000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:45000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
        #----------------------------------------------
        dataset_vieay_view= dataset[:50000].values
        values=dataset_vieay_view[:,5]
        n=len(values)
        start2_time = time.time()
        mergeSort(values,0,n-1) 
        end2_time = time.time()
        TIMMERMERGESORT.append(end2_time-start2_time)
        SIZEM.append(n)
        print("Done values: ",n)
#-----------------------------------------------------------------------------
        sizei=np.reshape(SIZEI, (13,1))
        sizeq=np.reshape(SIZEQ, (13,1))
        sizem=np.reshape(SIZEM, (13,1))
        #----------------------------------------------------
        TIMMERINSERTION=np.reshape(TIMMERINSERTION, (13,1))
        TIMMERQUICKSORT=np.reshape(TIMMERQUICKSORT, (13,1))
        TIMMERMERGESORT=np.reshape(TIMMERMERGESORT, (13,1))
        #---------------------------------------------------------------
        plotgraph.figure(figsize=(8,5))
        plotgraph.title('Time Complexity Insertion Sort vs Quick Sort vs Merge Sort', fontdict={'fontweight':'bold', 'fontsize': 18})
        plotgraph.plot(sizei, TIMMERINSERTION, color='blue', label='INSERTION')
        plotgraph.plot(sizeq, TIMMERQUICKSORT, color='yellow', label='QUICK')
        plotgraph.plot(sizem, TIMMERMERGESORT, color='green',label='MERGE')
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
def insertionSort(vie): 

    for i in range(1, len(vie)):
        keye = vie[i] 
        j = i-1
        while j >= 0 and keye < vie[j] : 
                vie[j + 1] = vie[j] 
                j -= 1
        vie[j + 1] = keye 
#-----------------------quicksort-----------------------------    
def quickSort(vie,low,high): 
    if low < high: 
        pi = partition(vie,low,high) 
        quickSort(vie, low, pi-1) 
        quickSort(vie, pi+1, high) 
    
def partition(vie,low,high): 
    i = ( low-1 )         
    pivot = vie[high]     
  
    for j in range(low , high): 
        if   vie[j] <= pivot: 
            i = i+1 
            vie[i],vie[j] = vie[j],vie[i] 
  
    vie[i+1],vie[high] = vie[high],vie[i+1] 
    return ( i+1 ) 

#------------------------mergesort--------------------------------------   
def mergeSort(vie,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(vie, l, m) 
        mergeSort(vie, m+1, r) 
        merge(vie, l, m, r) 
        
def merge(vie, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
   
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    
    for i in range(0 , n1): 
        L[i] = vie[l + i] 
  
    for j in range(0 , n2): 
        R[j] = vie[m + 1 + j] 
  
   
    i = 0      
    j = 0     
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            vie[k] = L[i] 
            i += 1
        else: 
            vie[k] = R[j] 
            j += 1
        k += 1
  

    while i < n1: 
        vie[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        vie[k] = R[j] 
        j += 1
        k += 1

#-----------------------------------------------------------------------------------------        
            
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





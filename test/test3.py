import numpy as np
import sys
import time
from medianLab import scripts
from mpmath.identification import prodstring
from scripts.naiveMedian import naiveMedianClass
from scripts.advancedMedian import advancedMedianClass
from scripts.rndMedian import rndMedianClass


title=["#","naive","rnd","advanced","t2/t1","t3/t1"]
sys.stdout=open("./docs/results.txt","a")
print("\ntest3:")

# test-sameItem
for i in title:
    print(i,end="\t")
print()
max_len=1500000
for i in range(0,10):



    arr=[max_len-100 for i in range(0,max_len)]
    arr1=arr.copy()
    arr2=arr.copy()


    m1=naiveMedianClass()
    start = time.time()
    mid1=m1.naiveMedian(arr1,int(len(arr)/2))
    end = time.time()
    cost1=m1.cost
    time1=end-start
    

    m2=rndMedianClass(max_len)
    start = time.time()
    mid2=m2.rndMedian(arr1,int(len(arr)/2))
    end = time.time()
    cost2=m2.cost
    time2=end-start


    m3=advancedMedianClass()
    start = time.time()
    mid3=m3.advancedMedian_QueueImpl(arr1,int(len(arr)/2))
    end = time.time()
    cost3=m3.cost
    time3=end-start



    if(mid1!=mid2 or mid3!=mid1):
        print("error")

    print(i,end="\t")
    print(cost1,end="\t")
    print(cost2,end="\t")
    print(cost3,end="\t")
    print("%.3f"%(100*(time2/time1)),end="\t")
    print("%.3f"%(100*(time3/time1)),end="\n")




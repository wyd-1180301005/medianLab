import numpy as np
import math as ma
from sympy import sieve
from scripts.advancedMedian import advancedMedianClass
from scripts.naiveMedian import naiveMedianClass
from scripts.naiveMedian import myQsort

class myHash():

    num=0
    mod=None
    a=None
    b=None

    def __init__(self,range) -> None:
        self.mod=[i for i in sieve.primerange(range, 100*range)]
        self.a=self.mod.copy()
        self.b=self.mod.copy()
        self.num=len(self.mod)
    
    def getHash(self,input,range):
        return ((self.a[np.random.randint(0,self.num)]*input+self.b[np.random.randint(0,self.num)])%self.mod[np.random.randint(0,self.num)])%range

class rndMedianClass():
    cost=0
    failure=0
    hash_func=None

    def __init__(self,max_len) -> None:
        self.hash_func=myHash(max_len)

    def rndMedian(self,arr,k):

        length=len(arr)

        # 对于长度特别小的情况的特判:
        if(length<=75):
            self.cost+=myQsort(arr,0,length)
            return arr[k]

        select_num=int(ma.sqrt(ma.sqrt((length*length*length))))
        while(True):
            
            # 选择n^(3/4)个放到数组之前
            self.cost+=select_num
            for i in range(0,select_num):
                pos=self.hash_func.getHash(i,length)

                if(pos>=select_num):
                    tmp=arr[pos]
                    arr[pos]=arr[i]
                    arr[i]=tmp

            # 将其排序
            self.cost+=myQsort(arr,0,select_num)
            # 根据期望,arr中的第k个元素,期望落在arr[0:selec_num]中的第(k/length)*select_num号元素的相邻区间内部

            expect_pos=int((k/length)*select_num)
            pos_l=max(int(expect_pos-ma.sqrt(length)),0)
            pos_h=min(int(expect_pos+ma.sqrt(length)),select_num-1)
            L=arr[pos_l]
            H=arr[pos_h]

            L_order=pos_l
            H_order=pos_h


            # 考察剩下的那些没被选中的元素
            # [L ...  H] ed ... SELEC_NUM)...LENGTH) 
            ed=pos_h+1
            self.cost+=length-select_num

            # 要对相等的情况进行特判:
            equal_H=0
            for i in range(select_num,length):
                # 要对相等情况进行特判,并且要最先进行该判断,以防L==H的情况
                if (arr[i]==H):
                    equal_H+=1
                # 不在选定区间内部
                elif(arr[i]<=L):
                    L_order+=1
                    H_order+=1
                # 在选定区间内部
                # 不能是大于等于 小于等于 否则在数组所有元素都是一样的情况下,选定区件大小会过于庞大
                elif(arr[i]<H):
                    H_order+=1

                    tmp=arr[ed]
                    arr[ed]=arr[i]
                    arr[i]=tmp
                    ed+=1

            # 如果arr中的第k号元素在[L,ed)中,且[L,ed)中元素的个数不超过4*select_num+1,排序arr[L:ed]并返回第arr[k-Lorder]
            # 否则重新开始,并且记failure+=1
            if(k in range(L_order,H_order+1) and (ed-pos_l)<=4*select_num+1):
                self.cost+=myQsort(arr,pos_l,ed)
                return arr[k-L_order+pos_l]
            # 不在区间内部,也有可能是缺省了大量euqal_H而导致的:
            # 1 2 3 3 [3 4 5 6 7 8] 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 10 11 12
            elif(k>H_order and k <= H_order+equal_H and(ed-pos_l)<=4*select_num+1):
                return H
            else:
                self.failure+=1

# # test rndMedian的正确性
# leng=100000
# for i in range(0,100):
#     arr=np.random.randint(0,3,10000)
#     arr1=arr.copy()
#     arr2=arr.copy()



#     m1=naiveMedianClass()
#     mid1=m1.naiveMedian(arr1,int(len(arr)/2))

#     m2=rndMedianClass(leng)
#     mid2=m2.rndMedian(arr,int(len(arr)/2))


#     if(mid2 !=  mid1):
#         print("error rnd")

#     # print-out
#     # print(mid1,end="\t")
#     # print(mid2,end="\t")
#     # print(mid3)
# print("end-test:rndMedian")
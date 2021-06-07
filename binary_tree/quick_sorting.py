"""
快速排序
http://data.biancheng.net/view/117.html
https://www.runoob.com/python3/python-quicksort.html
"""
import numpy as np
import time
import sys

# Python是有默认递归深度的，1000或者998(有争议)，
# 所以当测试集数据比较大时需要手动设置递归深度，
# 但也不是可以随便设置的，跟机器的性能有关
num = 100000
sys.setrecursionlimit(num)

def quickSort(arr, begin, end):
    if begin < end:
        i = begin
        j = end
        key = arr[begin]
        while i < j:
            while(( i < j ) and (arr[j] > key)):
                j = j - 1
            if i < j:
                arr[i] = arr[j]
                i = i + 1
        
            while((i < j) and (arr[i] < key)):
                i = i + 1
            if i < j:
                arr[j] = arr[i]
                j = j - 1
        
        arr[i] = key
        quickSort(arr, begin, i-1)
        quickSort(arr, i+1, end)


arr = np.random.randint(10000,size=100000)
quickSort(arr, 0, len(arr) - 1)
print(arr)

#! /usr/bin/env python3


def binary_search(list, item):
    low = 0                 #确定查找的范围
    high = len(list)-1

    while low <= high:
        mid = int((low + high)/2)   #查找中间的元素
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:              #二分缩小范围
            high = mid - 1
        else:
            low = mid + 1
    return None

def findSamllest(arr):
    smallest = arr[0]   #选择一个元素，假设其为最小值，并存储
    smallest_index = 0  #存储最小值对应的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):    #对数组进行排序
    newArr = []
    for i in range(len(arr)):
        smallest = findSamllest(arr)
        newArr.append(arr.pop(smallest))
    return newArr               #return 要空一个tab位置

my_list = [1,3,4,5,6,9]
print (binary_search(my_list,9))

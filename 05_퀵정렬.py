# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 02:01:47 2022

@author: yoonjung
"""

def quicksort(array):
    if len(array) <2: #원소가 0이거나 1개인경우는 정렬이 필요없다.
        return array
    else:
        pivot = array[0] #sort를 처음시작하는 기준원소 
        less = [i for i in array[1:] if i <= pivot] #기준원소가 처음부터 끝까지중에 다른원소보다 크거나 같다
        greater = [i for i in array[1:] if i > pivot] #기준원소가 처음부터 끝까지 중에 작다.
    return quicksort(less) + [pivot] + quicksort(greater)




arr = [10,5,2,3]
# print(quicksort(arr))

print(arr[0])
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 00:15:58 2022

@author: yoonjung
"""

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index 


arr = [3,4,25,25,346,6,75,23]

print(findSmallest(arr))

#one of smallest thing is '3' in that array. 
#so '3' has got index:0
#findSmallest print out index number->0

def selectionSort(arr):
    newArr = []  #작은순서대로 담을 배열을 생성
    for i in range(len(arr)): #arr 원소만큼 반복할 임시값 i
        smallest = findSmallest(arr) #findSmallest함수의 인덱스값 정의
        newArr.append(arr.pop(smallest)) #최소인덱스값을 하나씩 꺼내서 newArr에 담는다
    return newArr #newArr값 배열 출력

print(selectionSort([5,3,6,2,10])) #newArr값을 selectionSort함수에 넣은값은 작은원소값 순으로 정렬한다.

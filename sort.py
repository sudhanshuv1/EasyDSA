from utils import getRandomArray
import sys


# Bubble Sort

def bubbleSort():
    nums = getRandomArray(10, 'int', 0, 100)
    print('********** Bubble Sort **********\nUnsorted Array: ', nums)
    n = len(nums)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    print('Sorted Array: ', nums)

bubbleSort()



# Selection Sort

def selectionSort():
    nums = getRandomArray(10, 'int', 0, 150)
    print('********** Selection Sort **********\nUnsorted Array: ', nums)
    n = len(nums)
    for i in range(n):
        largest, index = -sys.maxsize-1, 0
        for j in range(n-i):
            if nums[j] > largest:
                largest = nums[j]
                index = j
        nums[index], nums[n-i-1] = nums[n-i-1], nums[index]
    print('Sorted Array: ', nums)

selectionSort()



# Insertion Sort

def insertionSort():
    nums = getRandomArray(10, 'int', 0, 200)
    print('********* Insertion Sort ***********\nUnsorted Array: ', nums)
    n = len(nums)
    for i in range(1, n):
        j = i-1
        number = nums[i]
        while j >= 0:
            if nums[j] > number:
                nums[j+1] = nums[j]
                j -= 1
            else:
                break
        nums[j+1] = number
    print('Sorted Array: ', nums)

insertionSort()


# Merge Sort

def merge(leftHalf, rightHalf):
    i,j=0,0
    sortedList = []
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            sortedList.append(leftHalf[i])
            i += 1
        else:
            sortedList.append(rightHalf[j])
            j += 1
    while i < len(leftHalf):
        sortedList.append(leftHalf[i])
        i += 1
    while j < len(rightHalf):
        sortedList.append(rightHalf[j])
        j += 1
    return sortedList

def mSort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums)//2
    leftHalf = mSort(nums[:mid])
    rightHalf = mSort(nums[mid:])
    return merge(leftHalf, rightHalf)

def mergeSort():
    nums = getRandomArray(10, 'int', 0, 250)
    print('************ Merge Sort *************\nUnsorted Array: ', nums)
    sortedNums = mSort(nums)
    print('Sorted Array: ', sortedNums)

mergeSort()


# Quick Sort

def partition(nums, start, end):
    pivot = nums[start]
    left, right = start+1, end-1
    while left <= right:
        if nums[left] <= pivot:
            left += 1
        elif nums[right] > pivot:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
    nums[start], nums[right] = nums[right], nums[start]
    return right

def qSort(nums, start, end):
    if start + 1 >= end:
        return
    pos = partition(nums, start, end)
    qSort(nums, start, pos)
    qSort(nums, pos+1, end)

def quickSort():
    nums = getRandomArray(10, 'int', 0, 300)
    print('************ Quick Sort *************\nUnsorted Array: ', nums)
    n = len(nums)
    qSort(nums, 0, n)
    print('Sorted Array: ', nums)

quickSort()
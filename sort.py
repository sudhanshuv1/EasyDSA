from utils import getRandomArray
import sys

'''
Bubble Sort
Time Complexity: O(n^2)
Space Complexity: O(1)
Stable: Yes
In-Place: Yes
'''

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


'''
Selection Sort
Time Complexity: O(n^2)
Space Complexity: O(1)
Stable: No
In-Place: Yes
'''

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


'''
Insertion Sort
Time Complexity: O(n^2)
Space Complexity: O(1)
Stable: Yes
In-Place: Yes
'''

def insertionSort():
    nums = getRandomArray(10, 'int', 0, 200)
    print('********* Insertion Sort ***********\nUnsorted Array: ', nums)
    n = len(nums)
    for i in range(1, n):
        j = i-1
        number = nums[i]# Bubble Sort

        while j >= 0:
            if nums[j] > number:
                nums[j+1] = nums[j]
                j -= 1
            else:
                break
        nums[j+1] = number
    print('Sorted Array: ', nums)

insertionSort()


'''
Merge Sort
Time Complexity: O(nlogn)
Space Complexity: O(n)
Stable: Yes
In-Place: No
'''

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


'''
Quick Sort
Time Complexity: O(nlogn)
Space Complexity: O(logn)
Stable: No
In-Place: Yes
'''

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


'''
Heap Sort
Time Complexity: O(nlogn)
Space Complexity: O(1)
Stable: No
In-Place: Yes
'''

def heapify(nums, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and nums[largest] < nums[l]:
        largest = l
    if r < n and nums[largest] < nums[r]:
        largest = r
    
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

def hSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapSort():
    nums = getRandomArray(10, 'int', 0, 350)
    print('************ Heap Sort *************\nUnsorted Array: ', nums)
    hSort(nums)
    print('Sorted Array: ', nums)

heapSort()
'''
Linear Search
Time Complexity: O(n)
Space Complexity: O(1)
'''

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


'''
Binary Search
Time Complexity: O(logn)
Space Complexity: O(1)
'''

def binarySearch(arr, target):
    start, end = 0, len(arr)
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def search():
    arr = [6, 32, 62, 63, 96, 101, 119, 203, 265, 279]
    target = 62
    print('Array:', arr)
    print(target, 'found by Linear Search at index:', linearSearch(arr, target))
    print(target, 'found by Binary Search at index:', binarySearch(arr, target))
    target = 100
    print(target, 'found by Linear Search at index:', linearSearch(arr, target))
    print(target, 'found by Binary Search at index:', binarySearch(arr, target))

search()
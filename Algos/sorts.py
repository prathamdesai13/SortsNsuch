# bunch of sorting algorithms
from DataStructs import MinHeap

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    
    for i in range(len(arr)):
        # print(arr)
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j+1)
    return arr

def recursive_bubble_sort(arr):
    """
    comparing consecutive elements and swapping accordingly pushes the largest
    element to the end, so we simply recurse on everything but the last element
    time. still operates in quadratic time, but recursive bubble sort just sounds funny
    """
    if len(arr) == 1:
        return arr
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            swap(arr, i, i + 1)
    return recursive_bubble_sort(arr[:len(arr) - 1]) + arr[len(arr) - 1:]

def insertion_sort(arr):
    # basically bubble sort
    sorted = [x for x in arr]
    for i in range(1, len(arr)):
        # print(sorted)
        for j in range(i):
            if (arr[i] < sorted[j]):
                swap(sorted, i, j)
    return sorted

def mergesort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return merge(arr[:1], arr[1:])
    mid = (len(arr) - 1)// 2
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))

def quick_sort(arr):

    pivot = (len(arr)) // 2 # pick pivot at midpoint of array
    if pivot == -1 or pivot == 0:
        return arr
    left_half = []
    right_half = []
    for i in range(len(arr)):
        if i != pivot:
            if arr[i] <= arr[pivot]:
                left_half.append(arr[i])
            else:
                right_half.append(arr[i])
    # print("left:", left_half)
    # print("right:", right_half)
    return quick_sort(left_half) + arr[pivot: pivot + 1] + quick_sort(right_half)
    

def merge(left_half, right_half):
    # print("left:", left_half)
    # print("right:", right_half)
    n = len(left_half)
    m = len(right_half)
    i = 0
    j = 0
    merged = []
    while i < n and j < m:
        if left_half[i] <= right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
    
    while i < n:
        merged.append(left_half[i])
        i += 1

    while j < m:
        merged.append(right_half[j])
        j += 1

    return merged

def heapsort(arr):
    """
    use a min heap to sort the elements of an array
    """
    pass

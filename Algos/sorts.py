

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    
    for i in range(len(arr)):
        print(arr)
        for j in range(i):
            if arr[i]  < arr[j]:
                swap(arr, i, j)
    return arr

def insertion_sort(arr):
    # basically bubble sort
    sorted = [x for x in arr]
    for i in range(1, len(arr)):
        print(sorted)
        for j in range(i):
            if (arr[i] < sorted[j]):
                swap(sorted, i, j)
    return sorted

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return merge(arr[:1], arr[1:])
    mid = (len(arr) - 1)// 2
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))


def merge(left_half, right_half):
    print("left:", left_half)
    print("right:", right_half)
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

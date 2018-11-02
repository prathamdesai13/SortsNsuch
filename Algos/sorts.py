

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def bubble_sort(arr):
	
	for i in range(len(arr)):
		for j in range(i):
			if arr[i]  < arr[j]:
				swap(arr, i, j)
	return arr

def mergesort(arr):

	if len(arr) == 2:
		return merge(arr[0:1], arr[1:])

	else:

		mid = len(arr) // 2
		return merge(mergesort(arr[:mid + 1]), mergesort(arr[mid + 1:]))

def merge(left_half, right_half):
	n = len(left_half)
	m = len(right_half)
	i = 0
	j = 0
	merged = []
	while i < n and j < m:
		if left_half[i] > right_half[j]:
			merged.append(left_half[i])
			i += 1
		else:
			merged.append(right_half[j])
			j += 1
	return merged
	
		
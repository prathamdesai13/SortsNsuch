

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

	if len(arr) == 1:
		return arr

	else:

		mid = len(arr) // 2
		return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))

def merge(left_half, right_half):
	n = len(left_half)
	m = len(right_half)	
	if n == 1 and m == 1:
		if left_half[0] > right_half[0]:
			return right_half + left_half
		return left_half + right_half

	elif n == 1:
		for i in range(m):
			if right_half[i] > left_half[0]:
				return right_half[:i]

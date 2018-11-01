

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
		print(arr)
		return arr
	
	mid = len(arr) // 2
	
	mergesort(arr[:mid+1])
	mergesort(arr[mid+1:])



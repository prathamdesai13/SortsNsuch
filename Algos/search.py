
def linear_search(arr, x):
	
	for i, e in enumerate(arr):
		if e == x:
			return i

	print("Item {} not found in array".format(x))

def binary_search(arr, left, right, x):
	# arr must be sorted
	if right < left:
		print("Item {} not found in array".format(x))
		return None
	
	mid = (left + right) // 2
		
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return binary_search(arr, left, mid - 1, x)
	else:
		return binary_search(arr, mid + 1, right, x)


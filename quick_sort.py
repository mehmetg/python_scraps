
import random

def partition(arr, start, end, pivot = None):
	if pivot == None: pivot = arr[end]
	left = start
	right = end - 1
	while (left < right):
		while(left< right and arr[left] < pivot): left += 1
		while(left< right and arr[right]> pivot): right -= 1
		if(right < left): 
			break
		else:
			arr[left], arr[right] = arr[right], arr[left]
	arr[end], arr[left] = arr[left], arr[end]
	return left
def _qsort(arr, start, end):
	if start >= end:
		return
	p = partition(arr, start, end)
	_qsort(arr,start,p-1)
	_qsort(arr,p+1, end)
def main():
	a = range(-15,16)
	random.shuffle(a)
	print(a)
	_qsort(a,0,len(a)-1)
	print(a)

if __name__ == '__main__':
	main()
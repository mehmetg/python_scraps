
import random

def partition_old(arr, start, end, pivot = None):
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
def qsort_old(arr, start, end):
	if start >= end:
		return
	p = partition(arr, start, end)
	qsort(arr,start,p-1)
	qsort(arr,p+1, end)

def partition(arr, start, end, pivot = None):
	if pivot == None: pivot = arr[end]
	while start < end:
		while (start < end) and (arr[start] < pivot): start += 1
		while (start < end) and (arr[end] > pivot): end -= 1
		if(arr[start] > arr[end]):
			arr[start], arr[end] = arr[end], arr[start]
	return start

def qsort(arr, start, end):
	if(start >= end):
		return
	p_idx = partition(arr,start,end, arr[(start+end)//2])
	qsort(arr, start, p_idx - 1)
	qsort(arr, p_idx + 1, end)

def main():
	a = range(-15,16)
	
	#a = a + a[:len(a)//4] + a[(len(a)//2):]
	
	random.shuffle(a)
	print(a)
	#print(partition(a,0,len(a)-1))
	#print(a)
	qsort(a,0,len(a)-1)
	print(a)

if __name__ == '__main__':
	main()
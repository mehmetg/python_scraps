
import random

def binary_search(arr, target, start = 0, end = None):
	if end == None: end = len(arr)-1
	
	
	mid = (start + end) // 2
	if start >= end and arr[mid] != target:
		#Not found return None
		return None
	if(arr[mid] < target):
		start = mid + 1
	elif (arr[mid] > target):
		end = mid - 1
	else:
		return mid
	return binary_search(arr, target, start, end)

def main():
	r = []
	a = range(-109,120)
	r[:] = a + [121,222]
	#print(binary_search(a,119))
	random.shuffle(r)
	
	for t in r:
		try:
			if a[binary_search(a,t)] != t:
				print("Failed!")
				print("target {}".format(t))
				print("found {}".format(a[binary_search(a,t)]))
		except Exception, e:
			print(e)
	


if __name__ == '__main__':
	main()
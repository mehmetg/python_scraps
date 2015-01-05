import random

def merge_sort(arr):
	if(len(arr) <= 1):
		return arr
	left = arr[:len(arr)//2]
	right = arr[len(arr)//2:]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left,right)

def merge(left,right):
	#print(left)
	#print(right)
	#print("__")
	arr =  []
	while len(left) or len(right):
		while len(left):
			if (not len(right)) or left[0] < right[0]:
				arr.append(left.pop(0))
			else:
				break
		while len(right):
			if not len(left) or right[0] < left[0]:
				arr.append(right.pop(0))
			else:
				break
	return arr
def main():
	a = range(13,-10,-1)
	b = range(0,2)
	random.shuffle(a)
	random.shuffle(b)
	print(a)
	#print(b)
	print(merge_sort(a))

if __name__ == '__main__':
	main()
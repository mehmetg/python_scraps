import random

def selection_sort(arr):
	size = len(arr)
	for i in xrange(size):
		min_idx = i
		for j in xrange(i + 1, size):
			if(arr[j] < arr[min_idx]):
				min_idx = j
		if min_idx != i:
			arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
	a = range(-5000,5000)
	random.shuffle(a)
	print(a)
	selection_sort(a)
	print(a)

if __name__ == '__main__':
	main()
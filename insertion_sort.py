import random

def insertion_sort(arr):
	size = len(arr)
	for i in range(size):
		for j in range(i, 0, -1):
			if(arr[j] < arr[j-1]):
				arr[j], arr[j-1] = arr[j-1], arr[j]
			else:
				break


def main():
	a = range(-5,4)
	random.shuffle(a)
	print(a)
	insertion_sort(a)
	print(a)

if __name__ == '__main__':
	main()
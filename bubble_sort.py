import random


def bubble_sort(arr):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(arr)-1):
			if arr[i+1] < arr[i]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				swapped = True



def main():
	a = range(-5,5)
	random.shuffle(a)
	print(a)
	bubble_sort(a)
	print(a)


if __name__ == '__main__':
	main()
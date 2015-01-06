import random

def stooge_sort(arr, start = 0, end = None):
	if end == None: end = len(arr)-1
	count = end - start
	if count > 1:
		if(arr[start] > arr[end]):
			arr[start], arr[end] = arr[end], arr[start]
		section_offset = (end - start + 1) // 3
		section_end = end - section_offset
		section_start = start + section_offset
		stooge_sort(arr, start, section_end)
		stooge_sort(arr, section_start, end)
		stooge_sort(arr, start, section_end)
	elif count == 1:
		if(arr[start] > arr[end]):
			arr[start], arr[end] = arr[end], arr[start]
	else:
		return

def main():
	s = range(-5,6)
	random.shuffle(s)
	print(s)
	stooge_sort(s)
	print(s)

if __name__ == '__main__':
	main()
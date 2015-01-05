
import heapq
import random

class myHeapContainer(list):
	heap = None
	is_max_heap = None
	def _is_in_order(self, parent, child):
		comp_val = parent > child
		#print comp_val
		if self.is_max_heap:
			return comp_val
		else:
			return (not comp_val)

	def __init__(self, arr = None, is_max = False):
		self.is_max_heap = is_max
		self.heap = arr
		if(arr):
			self._heapify()
		else:
			self.heap = []

	def __len__(self):
		return len(self.heap)
	def  _siftdown(self, root, child):
		parent = (child - 1) >> 1
		while parent >= root:
			if not self._is_in_order(self.heap[parent], self.heap[child]):
				self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
				child = parent
				parent = (child - 1) >> 1
			else:
				break
	def _siftup(self, root, length = None):
		c_pos = root * 2 + 1
		if length == None:
			tail = len(self)
		else:
			tail = length

		while c_pos < tail:
			r_pos = c_pos + 1
			if r_pos < tail and self._is_in_order(self.heap[r_pos], self.heap[c_pos]):
				c_pos = r_pos
			if not self._is_in_order(self.heap[root], self.heap[c_pos]):
				self.heap[c_pos], self.heap[root] = self.heap[root], self.heap[c_pos]
				root = c_pos
				c_pos = root * 2 + 1
			else:
				break 

	def _heapify(self):
		for parent in xrange(len(self)//2,-1,-1):
			self._siftup(parent)

	def heappush(self, item):
		self.heap.append(item)
		self._siftdown(0, len(self)-1)
	def heappop(self):
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		retval = self.heap.pop()
		self._siftup(0)
		return retval
	def heapsort(self, arr, is_max = False):
		self.is_max_heap = is_max
		self.heap = arr
		self._heapify()

		for i in xrange(len(arr), 0, -1):
			self.heap[0], self.heap[i-1] = self.heap[i-1], self.heap[0]
			self._siftup(0, i-1)


def main():
	arr = []
	a = range(10,0,-1)
	arr[:] = a
	random.shuffle(arr)
	print(arr)
	h = myHeapContainer(arr, False)
	print(h.heap)
	sarr = []
	while len(h):
		sarr.append(h.heappop())
	print(sarr)
	arr[:] = a
	h.heapsort(arr)
	print(arr)
	arr[:] = a
	h.heapsort(arr, True)
	print(arr)

	'''
	print("_______")
	

	
	arr = range(20,0,-1)
	h = myHeapContainer(None, True)
	for x in arr:
		h.heappush(x)
		heapq.heappush(hq, x)
	print(h.heap)
	print(hq)
	
	while(len(h)):
		h.heappop()
		heapq.heappop(hq)
		print(h.heap)
		print(hq)
	'''


if __name__ == '__main__':
	main()



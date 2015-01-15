class MultiStack(object):
	arr = None
	tops = None

	def __init__(self,num_stacks):
		self.arr = []
		self.tops = [None] * num_stacks

	def push(self, s_idx, val):
		if self.arr:
			arr_max = len(self.arr) - 1
		else:
			arr_max = -1

		if self.tops[s_idx] != None:
			self.tops[s_idx] += 3
		else:
			self.tops[s_idx] = s_idx
		
		if self.tops[s_idx] > arr_max:
			#print(self.tops[s_idx], arr_max)
			self.arr += ([None] * (self.tops[s_idx] - arr_max))
			#print(self.tops[s_idx], len(self.arr))
			self.arr[self.tops[s_idx]] = val
	def pop(self,s_idx):
		if self.tops[s_idx] != None:
			ret = self.arr[self.tops[s_idx]]
			self.tops[s_idx] -= 3
			if self.tops[s_idx] < 0:
				self.tops[s_idx] = None
		else:
			ret = None
		return ret
	def peek(self, s_idx):
		if self.tops[s_idx] != None:
			ret = self.arr[self.tops[s_idx]]
		else:
			ret = None
		return ret
	def get_size(self, s_idx):
		if(self.tops[s_idx]) != None:
			ret = (self.tops[s_idx] - s_idx) / 3
		else:
			ret = 0
		return ret

class StackWithMin(object):
	arr = None
	stack_min = None
	stack_ptr = None
	def __init__(self):
		self.arr = []
		self.stack_ptr = -1

	def push(self, val):
		if self.stack_min == None or self.stack_min > val:
			self.stack_min = val
		self.stack_ptr += 1
		if self.stack_ptr < len(self.arr):
			self.arr[self.stack_ptr] = (val, self.stack_min)
		else:
			self.arr.append((val, self.stack_min))

	def peek(self):
		if self.stack_ptr >= 0 and self.stack_ptr < len(self.arr):
			return self.arr[self.stack_ptr][0]
		else:
			return None
	def pop(self):
		if self.stack_ptr >= 0:
			ret = self.arr[self.stack_ptr]
			self.stack_min = ret[1]
			ret = ret[0]
			self.stack_ptr -= 1
		else:
			ret = None
		return ret
	def get_min(self):
		return self.stack_min
	def get_size(self):
		return (self.stack_ptr+1)

class Stack(object):
	arr = None
	stack_ptr = None
	def __init__(self):
		self.arr = []
		self.stack_ptr = -1

	def push(self, val):
		self.stack_ptr += 1
		if self.stack_ptr < len(self.arr):
			self.arr[self.stack_ptr] = val
		else:
			self.arr.append(val)

	def peek(self):
		if self.stack_ptr >= 0 and self.stack_ptr < len(self.arr):
			return self.arr[self.stack_ptr]
		else:
			return None
	def pop(self):
		if self.stack_ptr >= 0:
			ret = self.arr[self.stack_ptr]
			self.stack_ptr -= 1
		else:
			ret = None
		return ret
	def get_min(self):
		return self.stack_min
	def get_size(self):
		return (self.stack_ptr+1)
	def sort_desc(self):
		temp = Stack()
		while self.get_size() > 0:
			val = self.pop()
			if(temp.get_size() <= 0 or temp.peek() < val):
				temp.push(val)
			else:
				while temp.get_size() > 0 and temp.peek() > val:
					self.push(temp.pop())
				temp.push(val)
		temp.arr, self.arr = self.arr, temp.arr
		temp.stack_ptr, self.stack_ptr = self.stack_ptr, temp.stack_ptr

class StackOfStacks():
	stacks = None
	max_stack_size = None

	def __init__(self, max_size):
		self.stacks = []
		self.max_stack_size = max_size
	def push(self, val):
		if len(self.stacks) <= 0 or self.stacks[-1].get_size() >= self.max_stack_size:
			self.stacks.append(Stack())
		self.stacks[-1].push(val)

	def pop(self):
		if(len(self.stacks)):
			ret = self.stacks[-1].pop()
			if(self.stacks[-1].get_size() <= 0):
				self.stacks.pop(-1)
		else:
			ret = None
		return ret
	def pop_at(self, s_idx):
		if s_idx < len(self.stacks):
			ret = self.stacks[s_idx].pop()
			if(self.stacks[s_idx].get_size() <= 0):
				self.stacks.pop(s_idx)
		else:
			ret = None
		return ret

class TowerStack(Stack):
	def push(self, val):
		top = self.peek()
		if top is not None and top < val:
			raise Exception("Tower push error! Val > Top of Stack!")
		else:
			super(TowerStack, self).push(val)
def move_towers(num, src, buf, dst):
	if(num < 1):
		return
	move_towers(num-1, src, dst, buf)
	move_top(src, dst)
	move_towers(num-1, buf, src, dst)
def move_top(src, dst):
	disk = src.pop()
	if disk is not None:
		dst.push(disk)
def solve_tower_of_hanoi():
	n = 4
	towers = []
	for i in xrange(3):
		towers.append(TowerStack())
	for i in xrange(n):
		towers[0].push(n-i)
	for tower in towers:
		print(tower.arr[:tower.stack_ptr+1])
	move_towers(n, towers[0], towers[1], towers[2])
	for tower in towers:
		print(tower.arr[:tower.stack_ptr+1])
class myQueue(object):
	s1 = s2 = None

	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def queue(self, val):
		size1 = self.s1.get_size()
		size2 = self.s2.get_size() 
		if(size1 == 0 and size2 > 0):
			while size2:
				self.s1.push(self.s2.pop())
				size2 = self.s2.get_size()
		self.s1.push(val)
	def dequeue(self):
		size1 = self.s1.get_size()
		size2 = self.s2.get_size() 
		if(size2 == 0 and size1 > 0):
			while size1:
				self.s2.push(s1.pop())
				size1 = self.s1.get_size()
		val = self.s2.pop()
		return val
	def peek(self):
		size1 = self.s1.get_size()
		size2 = self.s2.get_size() 
		if(size2 == 0 and size1 > 0):
			while size1:
				self.s2.push(self.s1.pop())
				size1 = self.s1.get_size()
		val = self.s2.peek()
		return val

class Pet(object):
	CAT = 0
	DOG = 1
	species = None
	def __init__(self, spec):
		self.species = spec

from linked_lists import LList, Node
class PetQueue(LList):
	def __init__(self):
		self.pq = LList()
	def enqueue(self, pet):
		self.pq.append(pet)
	def dequeueAny(self):
		return self.pq.pop()
	def peek(self):
		return self.pq.head
	def _dequeue(self, spec):
		node = self.pq.head
		prev = None
		if node:
			while node:
				if node.data.species == spec:
					break
				prev = node
				node = node.next_node
			if(prev == None):
				node = self.pq.pop()
			elif node:
				prev.next_node = node.next_node
		else:
			node = None
		return node
	def dequeueCat(self):
		return self._dequeue(Pet.CAT)
	def dequeueDog(self):
		return self._dequeue(Pet.DOG)


	



def main():

	'''
	s = MultiStack(3)
	for i in xrange(30):
		s.push(i%3, (30-i))
		print(s.peek(i%3))
	
	for i in xrange(3):
		print(s.get_size(i))
	for i in xrange(3):
		p = s.pop(i)
		while p != None:
			print(p)
			p=s.pop(i)
	for i in xrange(3):
		print(s.get_size(i))
	
	import random
	s = Stack()
	for a in xrange(15):
		s.push(random.randrange(-100,100))
		print(s.get_min())
		#raw_input()
	print(s.arr)
	a = s.pop()
	while a != None:
		print(s.get_min())
		raw_input()
		a = s.pop()
		print(a)
	
	ss = StackOfStacks(5)

	for i in xrange(13):
		ss.push(i)
		#print("num stacks {}".format(len(ss.stacks)))
	print("pop from 1")
	for i in xrange(6):
		print(ss.pop_at(1))
		#print("num stacks {}".format(len(ss.stacks)))
	print("pop overall")
	
	for i in xrange(20):
		print(ss.pop())
		#print("num stacks {}".format(len(ss.stacks)))
	
	solve_tower_of_hanoi()
		s = myQueue()
	for i in xrange(20):
		s.queue(i)
	for i in xrange(15):
		print("peek: {}".format(s.peek()))
		print("dequeue: {}".format(s.dequeue()))
	for i in xrange(20):
		s.queue(i)
	for i in xrange(34):
		print("peek: {}".format(s.peek()))
		print("dequeue: {}".format(s.dequeue()))
	'''
	import random
	pq = PetQueue()
	for i in xrange(1):
		for x in xrange(10):
			n  = Node(Pet(0))
			print(n.data.species)
			pq.enqueue(n)
		print("--------")
		for i in xrange(10):
			n = pq.dequeueDog()
			if n:
				print(n.data.species)
			else:
				print(None)
		for i in xrange(10):
			n = pq.dequeueCat()
			if n:
				print(n.data.species)
			else:
				print(None)
if __name__ == '__main__':
	main()
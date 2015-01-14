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

class Stack(object):
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
		if self.stack_ptr < len(self.arr):
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
	'''
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

if __name__ == '__main__':
	main()
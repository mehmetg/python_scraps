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
def main():
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



if __name__ == '__main__':
	main()
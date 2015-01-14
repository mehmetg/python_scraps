from functools import total_ordering


@total_ordering
class Node(object):
	data = None
	prev_node = None
	next_node = None

	def __init__(self, data = None):
		self.data = data

	def __lt__(self, other):
		if other:
			return self.data < other.data
		else:
			return False
	def __eq__(self, other):
		if other:
			return self.data == other.data
		else:
			return self is None
	def __gt__(self, other):
		if other:
			return self.data > other.data
		else:
			return False
	def __le__(self, other):
		if other:
			return self.data <= other.data
		else:
			return False
	def __ge__(self, other):
		if other:
			return self.data >= other.data
		else:
			return False
	def __str__(self):
		if(self):
			return str(self.data)
		else:
			return None
class LList(object):
	head = None
	tail = None

	def __init__(self):
		pass

	def append(self, node):
		if (self.head):
			cur_node = self.head
			while cur_node.next_node:
				cur_node = cur_node.next_node
			cur_node.next_node = node
			node.prev_node = cur_node
		else:
			self.head = node
	def prepend(self, node):
		if (self.head):
			self.head.prev_node = node
			node.next_node = self.head
			self.head = node
		else:
			self.head = node
			self.head.next_node = None
	def to_array(self):
		ll = []
		c_node = self.head
		while c_node:
			ll.append(c_node.data)
			c_node = c_node.next_node
		return ll

	def remove_dups(self):
		s = self.head
		while s:
			sp = s
			sn = s.next_node
			while sn:
				if s == sn:
					sp.next_node = sn.next_node
					sn = sp.next_node
				else:
					sp = sn
					sn  = sn.next_node 
			s = s.next_node
	def return_kth_last_itr(self,k):
		cur = self.head
		lead = None
		lead_count = 0
		lead = cur
		while lead and lead_count < (k-1):
			lead = lead.next_node
			lead_count += 1

		if(lead_count < (k-1)):
			return None

		while lead:
			lead = lead.next_node
			if(lead):
				cur = cur.next_node
		return cur
	def return_kth_last_rec(self, k, node, kth_last_node):
		print(kth_last_node)

		if(node.next_node):
			count = 1 + self.return_kth_last_rec(k, node.next_node, kth_last_node)
			if(count == k):
				kth_last_node.data = node.data
			return count
		else:
			return 1
	def pop(self):
		if(self.head):
			node = self.head
			self.head = self.head.next_node
		else:
			node = None
		return node
	def partition(self,pivot):
		node = self.pop()
		lt_head = None
		lt_tail = None
		ge_head = None
		ge_tail = None
		while node:
			if(node.data < pivot):
				if lt_head:
					lt_tail.next_node = node
					lt_tail = node
				else:
					lt_head = node
					lt_tail = node
				lt_tail.next_node = None
			elif(node.data >= pivot):
				if ge_head:
					ge_tail.next_node = node
					ge_tail = node
				else:
					ge_head = node
					ge_tail = node
				ge_tail.next_node = None
			node = self.pop()
		lt_tail.next_node = ge_head
		self.head = lt_head

	def make_loopy(self,p=0):
		#loop to the pth element of the list
		node = self.head
		if (node):
			c = 0
			tar = None
			tail = None
			while node:
				if(c == p):
					tar = node
				if(node.next_node == None):
					node.next_node = tar
					break
				node = node.next_node
				c += 1

	def find_loop_start(self):
		fr = sr = self.head

		while sr and fr and fr.next_node:
			#print(sr, fr)
			sr = sr.next_node
			fr = fr.next_node.next_node
			if(sr is fr):
				#print("collision")
				#raw_input()
				break
		if(sr is not fr):
			return -1
		else:
			sr = self.head
			#print(sr)
			#print(fr)
			count = 0
			while sr and fr and sr is not fr:
				sr = sr.next_node
				fr = fr.next_node
				count += 1
			if sr is not fr:
				return -1
			else:
				#print("----")
				#print(sr)
				#print(fr)
				return count
	def is_palindrome(self):
		sr = self.head
		fr = self.head
		t = LList()
		count = 0
		while sr and fr and fr.next_node:
			node = sr
			sr = sr.next_node
			fr = fr.next_node.next_node
			if(fr):
				t.prepend(node)
				count += 1
			else:
				break
		pr = t.head
		while sr and pr:
			if sr != pr:
				return False
			sr = sr.next_node
			pr = pr.next_node
		return True



def get_length_simple_ll(node):
	count = 0
	while node:
		count += 1
		node = node.next_node
	return count
def pad_zero_simple_ll(node, p):
	if node:
		for i in xrange(p):
			pad = Node(0)
			pad.next_node = node.next_node
			node.next_node = pad
			pad.data = node.data
			node.data = 0

def prep_addition(num1, num2):
	len1 = get_length_simple_ll(num1)
	len2 = get_length_simple_ll(num2)
	p = len1 - len2
	if p > 0:
		pad_zero_simple_ll(num2, p)	
	elif p < 0:
		pad_zero_simple_ll(num1, -p)
	
	

def add_ll_numbers_rec_lsd_first(num1, num2, carry):
	
	if num1 == None and num2 == None and carry == 0:
		return None
	
	val = carry

	if num1:
		val += num1.data 
		next_num1 = num1.next_node
	else:
		next_num1 = None

	if num2:
		val += num2.data
		next_num2 = num2.next_node
	else:
		next_num2 = None

	carry = 1 if val > 9 else 0
	#print(val, next_num1, next_num2, carry)
	val = val % 10
	new_digit = Node(val)
	
	#raw_input()
	part_sum = add_ll_numbers_rec_lsd_first(next_num1, next_num2, carry)
	
	new_digit.next_node = part_sum
	part_sum = new_digit

	return part_sum

		
def _add_ll_numbers_rec_lsd_last(num1, num2, carry):
	if(num1 == None and num2 == None):
		carry[0] = 0
		return None
	#equal length asssumes the above statement holds... num2 check is redundant above
	part_sum = _add_ll_numbers_rec_lsd_last(num1.next_node, num2.next_node, carry)
	val = num1.data + num2.data + carry[0]
	carry[0] = 1 if val > 9 else 0
	val = val % 10
	new_digit = Node(val)
	new_digit.next_node = part_sum
	part_sum = new_digit
	return part_sum

def add_ll_numbers_rec_lsd_last(num1, num2):
	carry = [0]
	prep_addition(num1, num2)
	print_simple_ll(num1, False)
	print_simple_ll(num2, False)
	result = _add_ll_numbers_rec_lsd_last(num1,num2, carry)
	if carry[0]:
		msd = Node(carry[0])
		msd.next_node = result
		result = msd
	return result
	
def print_simple_ll(node, LSD_head = True, max_nodes = None):
	arr = [] 
	count = False
	if max_nodes == None:
		count = False
		max_nodes = 1
	else:
		count = True
	node_count = 0
	while node and node_count < max_nodes:
		if(LSD_head):
			arr.insert(0, node.data)
		else:
			arr.append(node.data)
		node = node.next_node
		node_count += 1 if count else 0
	print arr



def main():
	import random
	num1 = LList()
	num2 = LList()
	

	#for x in xrange(1):
	#	num1.append(Node(random.randrange(0,10)))
	#print_simple_ll(num1.head, False)
	for i in xrange(10):
		num2 = LList()
		for x in  xrange(10):
			num2.append(Node(x))
		print_simple_ll(num2.head, False)
		num2.make_loopy(i)
		print_simple_ll(num2.head, False, 24)
		print(num2.find_loop_start())
	#result = add_ll_numbers_rec_lsd_first(num1.head, num2.head, 0)
	#print_simple_ll(result)	
	#result = add_ll_numbers_rec_lsd_last(num1.head, num2.head)
	#print_simple_ll(result, False)	
if __name__ == '__main__':
	main()
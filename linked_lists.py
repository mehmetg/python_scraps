from functools import total_ordering


@total_ordering
class Node(object):
	data = None
	prev_node = None
	next_node = None

	def __init__(self, data = None):
		self.data = data

	def __lt__(self, other):
		return self.data < other.data
	def __eq__(self, other):
		return self.data == other.data
	def __gt__(self, other):
		return self.data > other.data
	def __le__(self, other):
		return self.data <= other.data
	def __ge__(self, other):
		return self.data >= other.data
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

def add_ll_numbers_rec(num1, num2, carry, LSD_head = True):
	if num1 == None and num2 == None and carry == 0:
		return None
	
	val = carry

	if num1:
		val += num1.data
		next_num1 = next_num1.next_node
	else:
		next_num1 = None

	if num2:
		val += num2.data
		next_num2 = num2.next_node
	else:
		next_num2 = None

	carry = 1 if val > 9 else 0
	val = val % 10
	new_digit = Node(val)
	part_sum = add_ll_numbers_rec(next_num1, next_num2, carry)
	if part_sum:
		new_digit.next_node = part_sum
		part_sum = new_digit
	else:
		part_sum = new_digit

	return part_sum



def main_old():
	import random
	my_ll = LList()
	arr = []

	for j in xrange(30):
		for i in xrange(4):
			arr.append(i)
	random.shuffle(arr)
	for x in arr:
		my_ll.append(Node(x))

	#print(my_ll.to_array())
	my_ll.remove_dups()
	print(my_ll.to_array())
	#print(my_ll.return_kth_last_itr(0))
	#node = Node(-999)
	#my_ll.return_kth_last_rec(3, my_ll.head, node)
	#print(node)
	my_ll.partition(1)
	print(my_ll.to_array())
def main():
	
if __name__ == '__main__':
	main()
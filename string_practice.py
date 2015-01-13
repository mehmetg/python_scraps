#Q1.1
def has_unique_chars_O_nsq(s):
	for i in xrange(len(s)):
		for j in xrange(len(s)):
			if(j != i and s[i] == s[j]):
				return False
	return True
def has_unique_chars_O_n(s):
	lookup = [None] * 255

	for c in s:
		c_code = ord(c)
		if(lookup[c_code]):
			return False
		else:
			lookup[c_code] = True
	return True
#Q1.2
def reverse_null_term_str(s):
	'''
	Def: length unknown, terminated  by Null(0) chars
	'''
	i = 0
	s = list(s)
	while s[i] != "\0":
		i += 1
	for j in xrange(i//2):
		 t = s[j]
		 s[j] = s[i-j-1]
		 s[i-j-1] = t
	return  "".join(s)
#Q1.3
def is_anagram(s, t):
	lk_s = [0] * 255
	lk_t = [0] * 255
	if(len(s) != len(t)):
		return False
	else:
		for i in xrange(len(s)):
			lk_s[ord(s[i])] += 1
			lk_t[ord(t[i])] += 1
		for i in xrange(len(lk_s)):
			if(lk_s[i] != lk_t[i]):
				return False
		return True
#Q1.4
def escape_space_n_sq(s):
	'''
	Assume Java rules:
	'''
	s = list(s)
	i = 0
	while i < len(s):
		if(s[i] == " "):
			#shiftdown by 2 and add %20
			end = len(s)
			s += ["",""]
			for  j in xrange(end-1,i,-1):
				s[j+2] = s[j]
			s[i] = "%"
			s[i+1] = "2"
			s[i+2] = "0"
			i += 3
		else:
			i +=1
		#print "".join(s)
		#print(len(s))
		#print(i)
	return "".join(s)

def escape_space_2n(s):
	l = 0
	for c in s:
		if c == " ":
			l += 2
	s = list(s)
	orig_len = len(s)
	s = s + ["-"] * l
	tail = len(s) - 1
	for i in xrange(orig_len-1,-1,-1):
		if s[i] != " ":
			s[tail] = s[i]
			tail -= 1
		else:
			s[tail] =   "0"
			s[tail-1] = "2"
			s[tail-2] = "%"
			tail -= 3
	return "".join(s)
#Q1.5
def str_compress(s):
	s = list(s)
	t = []
	i = 0
	s_len = len(s)
	while i < s_len and len(t) < s_len:
		j = i + 1
		while j < s_len and s[i] == s[j]:
			j += 1
		t += [s[i], str((j-i))]
		i = j

	if(s_len <= len(t)):
		t = s

	return "".join(t)
#Q1.6
def rotate_sq_matrix_by_90_deg_complicated(n_by_n):
	n = len(n_by_n)
	ub = n-1
	lb = 0
	while ub > lb:
		for j in range(lb, ub):
			#ul -> ur
			temp = n_by_n[j][ub]
			#print(j, ub, n_by_n[j][ub])
			#raw_input()
			n_by_n[j][ub] = n_by_n[lb][j]
			#ul -> ll
			n_by_n[ub][ub-j+lb], temp = temp, n_by_n[ub][ub-j+lb]
			#lr -> ll
			n_by_n[ub-j+lb][lb], temp = temp, n_by_n[ub-j+lb][lb]
			#lr -> ur
			n_by_n[lb][j] = temp
		ub -= 1
		lb += 1
		#break
def rotate_sq_matrix_by_90_deg(m):
	ub = len(m) - 1
	lb = 0

	while ub > lb:
		r = ub - lb
		#print(lb, ub, r)
		for i in xrange(r):	
			temp = m[lb+i][ub]
			m[lb+i][ub] = m[lb][lb+i]

			m[ub][ub-i], temp = temp, m[ub][ub-i]

			m[ub-i][lb], temp = temp, m[ub-i][lb]

			m[lb][lb+i] = temp
		#break
		ub -=1
		lb +=1
def	gen_sq_matrix(n):
	m = []
	l = []
	for i in xrange(n*n):
		if(i > 0 and i % n == 0):
			m.append(l)
			l = []
		l.append(i)
	if(len(l) > 0):
		m.append(l)
	return m
def mprint(matrix):
	for row in matrix:
		print "\t".join(str(x) for x in row)
#Q1.7
def gen_matrix(n,m):
	r = []
	mat = []
	for i in xrange(n*m):
		if i > 0 and i % m == 0:
			mat.append(r)
			r = []
		r.append(i)
	if(len(r)>0):
		mat.append(r)
	return mat 
def matrix_zero_out(mat):
	n = len(mat)
	m = len(mat[0])
	zero_rows = []
	zero_cols = []
	for r in xrange(n):
		if(r not in zero_rows):
			for c in xrange(m):
				if(c not in zero_rows):
					if mat[r][c] == 0:
						zero_rows.append(r)
						zero_cols.append(c)
	print zero_cols
	print zero_rows
	for zc in zero_cols:
		for i in xrange(n): mat[i][zc] = 0
	for zr in zero_rows:					
		for i in xrange(m): mat[zr][i] = 0
#Q1.8
def rotate_string(s, n):
	n = n % len(s)
	s = s[-n:] + s[:-n]
	return s

def rotate_string_in_place(s,n):
	l = len(s)
	n =  n % l
	s = list(s)
	for  i in range(0,n):
		s[i], s[l-n+i] =  s[l-n+i], s[i]
		#s[i], s[i-n] =  s[i-n], s[i]
	return "".join(s)

def is_rotation(r,s):
	return s in r+r 
def main_1p1():
	test_strings = ["abc", "aabc", "aaabbbccc", "aaa", "aaaaaaaaaaaaaz", "", " "]
	print("O(n**2):")
	for s in test_strings:
		print("{} has all unique chars: {}".format(s,has_unique_chars_O_nsq(s)))
	print("O(n):")
	for s in test_strings:
		print("{} has all unique chars: {}".format(s,has_unique_chars_O_n(s)))
def main_1p2():
	test_strings = ["abc", "aabc", "aaabbbccc", "aaa", "aaaaaaaaaaaaaz", "", " "]
	for s in test_strings:
		s += "\0"
		print(s)
		s = reverse_null_term_str(s)
		print(s)
def main_1p3():
	s1 = "111111111111111211111az"
	s2 = "a121111111111111111111z"
	print(is_anagram(s1,s2))
def main_1p4():
	s = ["","a b cdddd d", "a b b s s s s  s ssss          ", " ", "         s", "a        "]
	for ss in s:
		print("\"{}\"".format(ss))
		print(escape_space_2n(ss))
def main_1p5():
	s = "aaaaaaaaabcaaaaaaaccccccddddddb"
	print(s)
	print(str_compress(s))
def main_1p6():
	n = input()
	m = gen_sq_matrix(n)
	mprint(m)
	print("-----")
	rotate_sq_matrix_by_90_deg(m)
	mprint(m)

def main_1p7():
	import random
	m, n = 8, 6
	
	x = gen_matrix(n,m)
	x[0][0] = -1
	for i in xrange(2):
		zc = random.randrange(m)
		zr = random.randrange(n)
		x[zr][zc] = 0

	mprint(x)
	print("-----")
	matrix_zero_out(x)
	mprint(x)
def main_1p8():
	import random, string
	s = string.ascii_uppercase 
	n = random.randrange(len(s))
	r = rotate_string(s, n)
	
	print(s)
	print(r)
	print(is_rotation(r,s))
	r = list(r)
	random.shuffle(r)
	r = "".join(r)
	print(is_rotation(r,s))
def main():
	import random, string
	s = string.ascii_uppercase 
	n = random.randrange(len(s))
	r = rotate_string(s, 2)
	r2 = rotate_string_in_place(s, 2)
	print(s)
	print(r)
	print(r2)
	print(r==r2)
if __name__ == '__main__':
	main()
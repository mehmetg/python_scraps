class Foo(object):
	A = 1
	B = 2
	def __init__(self):
		self.class_var = "V"


def main():
	f = Foo()
	g = Foo()
	f.A = 12
	g.A = 33
	Foo.A = 34
	print("f.A: {}".format(f.A))
	print("g.A: {}".format(g.A))
	print("Foo.A: {}".format(Foo.A))
	print("f.class_var: {}".format(f.class_var))

if __name__ == '__main__':
	main()
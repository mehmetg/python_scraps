class TreeNode(object):
	
	def __init__(self, payload = None, children = 2):
		self.data = payload
		self.visited = False
		#left right, etc
		self.adjacent = [None] * children
def add_to_bin_search_tree(root, pl):
	if root and root.data:
		if pl > root.data:
			if(root.adjacent[1] is None):
				root.adjacent[1] = TreeNode()
			add_to_bin_search_tree(root.adjacent[1],pl)
		else:
			if(root.adjacent[0] is None):
				root.adjacent[0] = TreeNode()
			add_to_bin_search_tree(root.adjacent[0],pl)
	else:
		root.data = pl
def build_bin_search_tree(arr):
	root = TreeNode()
	for x in arr:
		add_to_bin_search_tree(root, x)
	return root
def print_bin_tree_in_order(root):
	if root:
		print_bin_tree_in_order(root.adjacent[0])
		print(root.data)
		print_bin_tree_in_order(root.adjacent[1])
def _is_bin_tree_balanced(root, threshold = 1):
	if root:
		r = _is_bin_tree_balanced(root.adjacent[0], threshold)
		#print(r)
		if r == -1: return -1
		l = _is_bin_tree_balanced(root.adjacent[1], threshold)
		#print(l)
		if l == -1 : return -1
		if abs(r-l) > threshold: 
			return -1
		else:
			return (max(r,l) + 1)
	else:
		return 0
def is_bin_tree_balanced(root, threshold = 1):
	if _is_bin_tree_balanced(root, threshold) == -1:
		return False
	else:
		return True
def route_available_dfs(graph, start, finish, visited = []):
	visited.append(start)
	if finish == start:
		return True
	for adj in graph[start]:
		#print(visited)
		if adj not in visited:
			if route_available_dfs(graph, adj, finish, visited):
				return True
	return False
def route_available_bfs(graph, start, finish):
	visited = []
	nq = []
	nq.append(start)
	while len(nq):
		#print(nq)
		#raw_input()
		n = nq.pop(0)
		if n not in visited:
			visited.append(n)
			if n == finish:
				return True
			for adj in graph[n]:
				if adj not in nq: nq.append(adj)
	return False

def main():
	'''
	import random
	r = False
	a = range(11)
	while not r:
		random.shuffle(a)
		#print(a)
		tree = build_bin_search_tree(a)
		#print_bin_tree_in_order(tree)
		r = is_bin_tree_balanced(tree, 1)
	
	print(r)
	print(a)
	'''
	g = [[1],[11,2],[4],[1],[5],[3],[9],[8],[],[7],[0],[]]
	print(route_available_dfs(g,6,6,[]))
	#print(g)
	print(route_available_bfs(g,6,6))
	#print(g)
if __name__ == '__main__':
	main()
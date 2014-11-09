import bisect
class DirectedGraph():
	def __init__(self):
		self.vetrex_map = dict()

	def hasVetrex(self, vetrex_name):
		return self.vetrex_map.has_key(vetrex_name)

	def addVetrex(self, vetrex_name):
		if not self.hasVetrex(vetrex_name):
			self.vetrex_map.update({vetrex_name:[]})

	def hasEdge(self, vetrex_name1, vetrex_name2):
		if not self.hasVetrex(vetrex_name1):
			return False
		if not self.vetrex_map.has_key(vetrex_name2):
			return False
		edges = self.vetrex_map[vetrex_name1]
		return bisect.bisect_right(edges, vetrex_name2) != -1

	def addEdge(self, vetrex_name1, vetrex_name2):
		if not self.hasVetrex(vetrex_name1):
			self.addVetrex(vetrex_name1)
		if not self.hasVetrex(vetrex_name2):
			self.addVetrex(vetrex_name2)

		edges1 = []
		edgees = self.vetrex_map[vetrex_name1]
		edges1.append(vetrex_name2)

def main():
		graph = DirectedGraph()

		graph.addEdge('name1','name2')

		print(graph.hasEdge('name1','name2'))


if __name__ == '__main__':
	main()
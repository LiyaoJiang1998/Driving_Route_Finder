# Student Name: Liyao Jiang
# Student ID: 1512445
# Section: EB1
# Student Name: Xiaolei Zhang
# Student ID: 1515335
# Section: B1
# Assignment1 Part1

from binary_heap import BinaryHeap
from breadth_first_search import get_path

# implementation of Dijkstra's Algorithm based on Pseudocode from class
def least_cost_path(graph, start, dest, cost):
	"""
	Find and return a least cost path in graph from start
	vertex to dest vertex.

	Efficiency: If E is the number of edges, the run-time is
	O( E log(E) ).

	Args:
		graph (Graph): The digraph defining the edges between the
			vertices.
		start: The vertex where the path starts. It is assumed
			that start is a vertex of graph.
		dest:  The vertex where the path ends. It is assumed
			that dest is a vertex of graph.
		cost:  A class with a method called "distance" that takes
			as input an edge (a pair of vertices) and returns the cost
			of the edge. For more details, see the CostDistance class
			description below.

	Returns:
		list: A potentially empty list (if no path can be found) of
		the vertices in the graph. If there was a path, the first
		vertex is always start, the last is always dest in the list.
		Any two consecutive vertices correspond to some
		edge in graph.
	"""

	# initialize reached as a empty dict
	reached = {}
	# an instance of BinaryHeap class, initially empty
	events = BinaryHeap()
	events.insert((start,start),0)  # vertex s burns at time 0
	while len(events) > 0 :
		(u,v), time = events.popmin()
		if v not in reached:
			reached[v] = u  # burn vertex v, record predecessor u
			nbr_list = graph.neighbours(v)
			for w in nbr_list:
				# new event: edge (v,w) started burning
				events.insert((v, w), time+cost.distance((v,w)))

	# using the get_path function from bfs file developed in class
	# get the path as a list, if no path then a empty list
	return get_path(reached, start, dest)

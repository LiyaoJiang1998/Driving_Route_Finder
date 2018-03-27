# Student Name: Liyao Jiang
# Student ID: 1512445
# Section: EB1
# Student Name: Xiaolei Zhang
# Student ID: 1515335
# Section: B1
# Assignment1 Part1

from graph import Graph

# Implementation of load_edmonton_graph
def load_edmonton_graph(filename):
	"""
	Loads the graph of Edmonton from the given file.

	Returns two items
	  graph: the instance of the class Graph() corresponding to the
		directed graph from edmonton-roads-2.0.1.txt
	  location: a dictionary mapping the identifier of a vertex to
		the pair (lat, lon) of geographic coordinates for that vertex.
		These should be integers measuring the lat/lon in 100000-ths
		of a degree.

	In particular, the return statement in your code should be
	  return graph, location
	(or whatever name you use for the variables).

	Note: the vertex identifiers should be converted to integers
	  before being added to the graph and the dictionary.
	"""

	# an instance of Graph class
	graph = Graph()
	# a dictionary mapping identifier to coordinates
	location = {}
	# open the file
	infile = open(filename, 'r')
	# read the file line by line
	infile_lines = infile.readlines()

	for eachline in infile_lines:
		# split each line by ","
		splitted = eachline.split(sep=",")
		# Vertex line starts with "V"
		if splitted[0] == "V":
			# convert the identifier to int as vertex indentifier
			v_iden = int(splitted[1])
			graph.add_vertex(v_iden)
			# convert coordinates to 100,000-ths degree int
			v_lati = int(float(splitted[2])*100000)
			v_long = int(float(splitted[3])*100000)
			# map the identifier to the coordinates
			location[v_iden] = (v_lati,v_long)

		# Edges line starts with "E"
		# We add edge for u and v in both directions
		# to realize an undirected graph
		if splitted[0] == "E":
			e_start = int(splitted[1])
			e_end = int(splitted[2])
			graph.add_edge((e_start,e_end))

	return graph, location

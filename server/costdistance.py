# Student Name: Liyao Jiang
# Student ID: 1512445
# Section: EB1
# Student Name: Xiaolei Zhang
# Student ID: 1515335
# Section: B1
# Assignment1 Part1

import math

# implementation of CostDistance class
class CostDistance:
	"""
	A class with a method called distance that will return the Euclidean
	between two given vertices.
	"""
	def __init__(self, location):
		"""
		Creates an instance of the CostDistance class and stores the
		dictionary "location" as a member of this class.
		"""
		self._location = location
	def distance(self, e):
		"""
		Here e is a pair (u,v) of vertices.
		Returns the Euclidean distance between the two vertices u and v.
		"""
		u = e[0]
		v = e[1]
		u_coordinate = self._location[u] 
		v_coordinate = self._location[v]
		dxsquare = (u_coordinate[0] - v_coordinate[0]) ** 2
		dysquare = (u_coordinate[1] - v_coordinate[1]) ** 2
		distance_euc = math.sqrt(dxsquare + dysquare)
		return distance_euc

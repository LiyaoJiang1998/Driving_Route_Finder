# Student Name: Liyao Jiang
# Student ID: 1512445
# Section: EB1
# Student Name: Xiaolei Zhang
# Student ID: 1515335
# Section: B1
# Assignment1 Part2
# Implemented based I our original part 1 submitted


from load_edmonton_graph import load_edmonton_graph
from costdistance import CostDistance
from least_cost_path import least_cost_path
import math

#import the serial communication and timeout
from serial import Serial
from time import sleep

# take a geographic coordinate and find the nearest vertex
# returns the vertex indentifier of the nearest vertex
def nearest_vertex(x,y,location):
	distance = []
	for v in location.items():
		dxsquare = (x - v[1][0]) ** 2
		dysquare = (y - v[1][1]) ** 2
		distance.append((v[0],math.sqrt(dxsquare + dysquare)))
	# sort the list of (vertex,distance) pair based on distance
	sorted_by_distance = sorted(distance, key=lambda tup: tup[1])
	return sorted_by_distance[0][0]

# load the edmonton graph file into a graph instance
# and loacation mapping vertex indentifier to (lat,lon)
graph, location = load_edmonton_graph("edmonton-roads-2.0.1.txt")
# create an instance of CostDistance
cost = CostDistance(location)

if __name__ == "__main__":
	# initailize the serial communication with a timeout of 1 sec
	with Serial("/dev/ttyACM0", baudrate=9600, timeout= 1) as ser:
		# wait for the next request after finished the current one
		while(True):
			line = ser.readline() # read the byte array through serial

			if not line:
				# test message
				print("timeout for empty line, restarting...")
				continue

			line_string = line.decode("ASCII") # decode to get string
			# Stripping off the newline and carriage return
			line_string = line_string.rstrip("\r\n")
			# split the line string
			received_line = line_string.split(sep=" ")
			# check if it is a request
			if (received_line[0]=="R") and (len(received_line)==5) :
				pass
			else:
				# after one second, timeout and start over
				# test message
				print("timeout for invalid Request, restarting...")
				print(line_string)
				continue
			# store the coordinate for start and end point read
			lat_1 = int(received_line[1])
			lon_1 = int(received_line[2])
			lat_2 = int(received_line[3])
			lon_2 = int(received_line[4])
			# find nearest start and end vertex
			start = nearest_vertex(lat_1,lon_1,location)
			end = nearest_vertex(lat_2,lon_2,location)
			# pass the instance of Graph and instance of CostDistance to
			# least_cost_path function to find a list of waypoints from
			# start to end
			waypoints_list = least_cost_path(graph, start, end, cost)
			waypoints_number = len(waypoints_list)

			if waypoints_number == 0:
				# if there is no path, send "N 0<\n>" and finish
				out_line = 'N'+' '+str(waypoints_number)+'\n'
				encoded = out_line.encode("ASCII")
				ser.write(encoded)
			else:
				# if there is a path,follow the protocol
				out_line = 'N'+' '+str(waypoints_number)+'\n'
				encoded = out_line.encode("ASCII")
				# test message
				print("sending N message",out_line)
				ser.write(encoded)
				for W in waypoints_list:
					# waiting for Acknoledgement send by client
					line = ser.readline() # read the byte array
					line_string = line.decode("ASCII") # decode to get string
					# Stripping off the newline and carriage return
					line_string = line_string.rstrip("\r\n")
					# split the line string
					received_line = line_string.split(sep=" ")
					if received_line[0] == 'A':
						# test message
						print("ack received")
						pass
					# holding for timeout if 'A' is not received
					else:
						# timeout after one second and start over
						# test message
						print("timeout waiting Ack, restarting...")
						break # skip the else part when time out
					# mapping identifier to (lat,lon)
					waypoints_coord = location[W]
					# send the waypoint
					out_line = 'W'+' '+str(waypoints_coord[0])+' '+str(waypoints_coord[1])+'\n'
					encoded = out_line.encode("ASCII")
					ser.write(encoded)
					# test message
					print("sending W message",out_line)
				else: # excuted if the loop ended normally without break
					# waiting for Acknoledgement for the last waypoint sent
					line = ser.readline() # read the byte array
					line_string = line.decode("ASCII") # decode to get string
					# Stripping off the newline and carriage return
					line_string = line_string.rstrip("\r\n")
					# split the line string
					received_line = line_string.split(sep=" ")
					if received_line[0] == 'A':
						# test message
						print("ack received")
						# send the end of program
						out_line = 'E'+'\n'
						encoded = out_line.encode("ASCII")
						ser.write(encoded)
						# test message
						print("sending E message",out_line)
					else:
						# timeout after one second and start over
						# test message
						print("timeout for last ack, restarting...")
						pass


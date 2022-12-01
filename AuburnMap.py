"""The point of AuburnMap.py is to use networkx, a python network Analysis library to create the map of the University."""
import networkx as nx
import matplotlib.pyplot as plt

auburnMap = nx.Graph()
"""adding our Nodes to the graph"""


auburnMap.add_node("Ross Hall")
auburnMap.add_node("Thatch At Haley")
auburnMap.add_node("Haley At Mell")
auburnMap.add_node("Mell")
auburnMap.add_node("The Quad")
auburnMap.add_node("Student Center")
auburnMap.add_node("Mell At The Quad")
auburnMap.add_node("Brown Kopel")

"""Connecting the Nodes with data from google maps. The weight is the distance between the nodes in meters."""
auburnMap.add_edge("Ross Hall", "Haley At Mell", weight = 126)
auburnMap.add_edge("Thatch At Haley", "Haley At Mell", weight = 215)
auburnMap.add_edge("Haley At Mell", "Mell", weight = 111)
auburnMap.add_edge("Mell", "Mell At The Quad", weight = 100)
auburnMap.add_edge("Thatch At Haley", "Student Center", weight = 200)
auburnMap.add_edge("Mell At The Quad", "Student Center", weight = 209)
auburnMap.add_edge("Thatch At Haley", "The Quad", weight = 207)
auburnMap.add_edge("Haley At Mell", "The Quad", weight = 178)
auburnMap.add_edge("Mell", "The Quad", weight = 105)
auburnMap.add_edge("Mell At The Quad", "The Quad", weight = 163)
auburnMap.add_edge("Student Center", "The Quad", weight = 200)
auburnMap.add_edge("Brown Kopel", "Ross Hall", weight = 106)
auburnMap.add_edge("Brown Kopel", "Thatch At Haley", weight = 126)



global nodeList 
nodeList = ["Ross Hall", "Thatch At Haley", "Haley At Mell", "Mell", "The Quad", "Student Center", "Mell At The Quad", "Brown Kopel"]



"""
shortestPath
Parameters: A Source Node and a destination Node
Returns: a List representing the shortest path between two locations.
"""
def shortestPath(source,destination):
    shortest = nx.shortest_path(auburnMap,source,destination)
    return shortest
"""
calcPathLength:
Parameters: A list of nodes describing the shortest path for source to destination
Returns: int value of meters between the path.
"""
def calcPathLength(shortestPath):
    length = 0
    i = 0
    while i < len(shortestPath) - 1:
        length += nx.path_weight(auburnMap,[shortestPath[i], shortestPath[i+1]], "weight")
        i += 1
    return length
"""
Result:
Parameters: Source Node Destination Node
Returns: Information of the shortest trip between two Nodes
"""
def result(source, destination):
    path = shortestPath(source, destination)
    pathString = ""
    for n in range(len(path)):
        pathString += path[n]
        pathString += " -> "
    pathLength = calcPathLength(path)
    #1.2 m/s is average walking speed
    estTime = pathLength / 1.2 / 60
    estTime = round(estTime, 2)
    pathStr = "The shortest distance between " + source + " and " + destination + " is " + pathString + "."
    lengthstr = "The current length between the two locations is " + str(pathLength) + "m."
    timestr = "Your estimated travel time is " + str(estTime) + " Minutes."
    strList = [pathStr, lengthstr, timestr]
    return strList
"""The point of Node.py is to use networkx, a python network Analysis library to create the map of the University."""
import networkx as nx
import matplotlib.pyplot as plt

auburnMap = nx.Graph()
"""adding our Nodes to the graph"""


auburnMap.add_node("Ross")
auburnMap.add_node("haleyAtThatch")
auburnMap.add_node("Haley At Mell")
auburnMap.add_node("Mell")
auburnMap.add_node("The Quad")
auburnMap.add_node("Student Center")
auburnMap.add_node("Mell At The Quad")

auburnMap.add_node("Parker")
auburnMap.add_node("EngDr")
auburnMap.add_node("GinnConcourse")
"""Connecting the Nodes with data from google maps. The weight is the distance between the nodes in meters."""
nx.add_path(auburnMap,["GinnConcourse","EngDr"],weight=230)
auburnMap.add_edge("GinnConcourse", "haleyAtThatch", weight = 250)
auburnMap.add_edge("EngDr", "Ross", weight = 145)
auburnMap.add_edge("Ross", "Haley At Mell", weight = 126)
auburnMap.add_edge("haleyAtThatch", "Haley At Mell", weight = 215)
auburnMap.add_edge("Haley At Mell", "Mell", weight = 111)
auburnMap.add_edge("Mell", "Mell At The Quad", weight = 100)
auburnMap.add_edge("haleyAtThatch", "Student Center", weight = 200)
auburnMap.add_edge("Student Center", "Parker", weight = 150)
auburnMap.add_edge("Mell At The Quad", "Student Center", weight = 209)
auburnMap.add_edge("haleyAtThatch", "The Quad", weight = 207)
auburnMap.add_edge("Haley At Mell", "The Quad", weight = 178)
auburnMap.add_edge("Mell", "The Quad", weight = 105)
auburnMap.add_edge("Mell At The Quad", "The Quad", weight = 163)
auburnMap.add_edge("Student Center", "The Quad", weight = 200)

global nodeList 
nodeList = ["GinnConcourse", "EngDr", "Ross", "haleyAtThatch", "Haley At Mell", "Mell", "The Quad", "Student Center", "Mell At The Quad", "Parker"]



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
    pathString = ''.join(path)
    pathLength = calcPathLength(path)
    #1.2 m/s is average walking speed
    estTime = pathLength / 1.2 / 60
    estTime = round(estTime, 2)
    pathStr = "The shortest distance between " + source + " and " + destination + " is " + pathString + "."
    lengthstr = "The current length between the two locations is " + str(pathLength) + "m."
    timestr = "Your estimated travel time is " + str(estTime) + " Minutes."
    strList = [pathStr, lengthstr, timestr]
    return strList
#result("The Quad", "Parker")
#print(calcPathLength(quadToParker))
#nx.draw(auburnMap, with_labels = True)
#plt.show()
class Graph:

    def __init__(self, adjList):
        self.adjList = adjList


class Node:

    def __init__(self, value):
        self.value = value


class Edge:

    def __init__(self, weight, node):
        self.node = node
        self.weight = weight
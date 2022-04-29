import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def isSafe(self, v, colour, c):
        # Check if 'c' is not already colored
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graphColourUtil(self, m, colour, v):
        # base case
        if v == self.V:
            return True

        # Try different colouring
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
        return False

    def graphColouring(self, m):
        # Initialize all color values as 0 (uncolored)
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == False:
            return False
        else:
            for i in range(self.V):
                print("The colour of", i, "is", colour[i])
            return True

    def addEdge(self, v, w):
        # Add edge from v to w
        self.graph[v][w] = 1
        self.graph[w][v] = 1

    def __str__(self) -> str:
        try:
            rows = len(self.graph)
            cols = len(self.graph[0])
            for i in range(rows):
                for j in range(cols):
                    if self.graph[i][j] == 1:
                        G.add_edge(i, j)
            nx.draw(G)
            plt.show()
        except:
            for i in range(self.V):
                for j in range(self.V):
                    print(self.graph[i][j], end=" ")
                print()


Graph = Graph(5)
Graph.addEdge(0, 1)
Graph.addEdge(0, 2)
Graph.addEdge(0, 3)
Graph.addEdge(1, 2)
Graph.addEdge(3, 4)
print(Graph)
print(Graph.graphColouring(3))

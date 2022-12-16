
"""Output of the code"""
#  Visitng :: A
# Visitng :: a
# Visitng :: C
# Visitng :: A
# Visitng :: v
# Visitng :: D
# Visitng :: a
# Visitng :: a
# Visitng :: A
# Visitng :: O
# Visitng :: C
# Visitng :: c
# Visitng :: C
# Visitng :: o
# Visitng :: a
# Visitng :: c
# Visitng :: A
# Visitng :: v
# Visitng :: T
# Target is reachable from source within max depth


from collections import defaultdict


# This class represents a directed graph using adjacency
# list representation
class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self, src, target, maxDepth):

        if src == target: return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            print("Visitng ::",i)
            if (self.DLS(i, target, maxDepth - 1)):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False


# Create a graph given in the above diagram
g = Graph(8);
g.addEdge('o', 'A')
g.addEdge('o', 'a')
g.addEdge('o', 'C')
g.addEdge('A', 'v')
g.addEdge('A', 'D')
g.addEdge('A', 'a')
g.addEdge('v', 'T')
g.addEdge('a', 'A')
g.addEdge('a', 'O')
g.addEdge('a', 'C')
g.addEdge('a', 'c')
g.addEdge('C', 'o')
g.addEdge('C', 'a')
g.addEdge('C', 'c')
g.addEdge('c', 'a')
g.addEdge('c', 'T')
g.addEdge('c', 'D')
g.addEdge('D', 'a')
g.addEdge('D', 'A')
g.addEdge('D', 'c')
g.addEdge('D', 'T')
g.addEdge('T', 'v')
g.addEdge('T', 'D')
g.addEdge('T', 'c')


target = 'T';
maxDepth = 10;
src = 'o'

if g.IDDFS(src, target, maxDepth) == True:
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")
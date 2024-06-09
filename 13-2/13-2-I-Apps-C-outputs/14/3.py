
def solve(n, m, pairs):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the given pairs of friends
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))

    # Find the minimum spanning tree of the graph
    mst = kruskal(graph)

    # Calculate the total cost of the MST
    total_cost = 0
    for edge in mst:
        total_cost += edge[2]

    return total_cost

# Kruskal's algorithm to find the minimum spanning tree of a graph
def kruskal(graph):
    # Sort the edges of the graph based on their weight
    edges = [(weight, vertex1, vertex2) for vertex1, edges in enumerate(graph) for vertex2, weight in edges]
    edges.sort()

    # Create a disjoint set to keep track of the connected components
    disjoint_set = DisjointSet(n)

    # Iterate through the sorted edges and add them to the MST only if they don't form a cycle
    mst = []
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            mst.append(edge)
            disjoint_set.union(vertex1, vertex2)

    return mst

# Disjoint-set data structure to keep track of the connected components
class DisjointSet:
    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n

    def find(self, vertex):
        if self.parents[vertex] == -1:
            return vertex
        else:
            self.parents[vertex] = self.find(self.parents[vertex])
            return self.parents[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.ranks[root1] > self.ranks[root2]:
                self.parents[root2] = root1
            else:
                self.parents[root1] = root2
                if self.ranks[root1] == self.ranks[root2]:
                    self.ranks[root2] += 1


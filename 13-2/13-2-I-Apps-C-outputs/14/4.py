
def solve(n, m, pairs):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the given pairs of friends
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))

    # Find the minimum spanning tree of the graph
    mst = kruskal(graph)

    # Calculate the total carbon dioxide emissions
    total_emissions = 0
    for edge in mst:
        total_emissions += edge[2]

    return total_emissions


def kruskal(graph):
    # Sort the edges of the graph by weight in non-decreasing order
    edges = [(weight, start, end) for start, adjacents in enumerate(graph) for end, weight in adjacents]
    edges.sort(key=lambda x: x[0])

    # Create a disjoint set data structure to store the components
    dsu = DisjointSet(len(graph))

    # Iterate through the sorted edges and add them to the MST
    mst = []
    for weight, start, end in edges:
        if dsu.find(start) != dsu.find(end):
            mst.append((start, end, weight))
            dsu.union(start, end)

    return mst


class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if self.ranks[x_root] > self.ranks[y_root]:
            self.parents[y_root] = x_root
        elif self.ranks[x_root] < self.ranks[y_root]:
            self.parents[x_root] = y_root
        else:
            self.parents[y_root] = x_root
            self.ranks[x_root] += 1


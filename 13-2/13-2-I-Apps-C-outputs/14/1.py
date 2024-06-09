
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
    ds = DisjointSet(len(graph))

    # Iterate through the sorted edges and add them to the MST
    mst = []
    for weight, start, end in edges:
        if ds.find(start) != ds.find(end):
            mst.append((start, end, weight))
            ds.union(start, end)

    return mst


class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, node):
        if self.parents[node] == node:
            return node
        else:
            self.parents[node] = self.find(self.parents[node])
            return self.parents[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.ranks[root1] > self.ranks[root2]:
                self.parents[root2] = root1
            elif self.ranks[root1] < self.ranks[root2]:
                self.parents[root1] = root2
            else:
                self.parents[root2] = root1
                self.ranks[root1] += 1


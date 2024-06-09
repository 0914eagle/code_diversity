
def solve(n, m, pairs):
    # Initialize a graph with n vertices
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for p, q, c in pairs:
        graph[p].append((q, c))
        graph[q].append((p, c))

    # Find the minimum spanning tree of the graph
    mst = kruskal(graph)

    # Calculate the total carbon dioxide emissions
    total_emissions = 0
    for edge in mst:
        total_emissions += edge[2]

    return total_emissions


def kruskal(graph):
    # Sort the edges of the graph by weight
    edges = [(weight, start, end) for start, adjacents in enumerate(graph) for end, weight in adjacents]
    edges.sort(key=lambda x: x[0])

    # Create a disjoint set to keep track of the connected components
    disjoint_set = DisjointSet(len(graph))

    # Iterate through the sorted edges
    mst = []
    for weight, start, end in edges:
        # Check if adding the edge would create a cycle
        if disjoint_set.find(start) != disjoint_set.find(end):
            # Add the edge to the MST
            mst.append((start, end, weight))

            # Union the connected components
            disjoint_set.union(start, end)

    return mst


class DisjointSet:
    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n

    def find(self, node):
        if self.parents[node] == -1:
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


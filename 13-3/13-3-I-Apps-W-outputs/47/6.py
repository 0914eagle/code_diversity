
def solve(N, towns):
    # Sort the towns by their x-coordinates
    sorted_towns = sorted(towns, key=lambda town: town[0])

    # Create a graph with an edge between each pair of towns
    graph = {}
    for i in range(N):
        graph[i] = []
    for i in range(N-1):
        for j in range(i+1, N):
            graph[i].append(j)
            graph[j].append(i)

    # Calculate the minimum cost of a spanning tree
    mst = kruskal(graph)
    cost = 0
    for edge in mst:
        town1, town2 = edge
        x1, y1 = towns[town1]
        x2, y2 = towns[town2]
        cost += abs(x1-x2) + abs(y1-y2)

    return cost

def kruskal(graph):
    # Create a priority queue to store the edges of the graph
    pq = []
    for node in graph:
        for neighbor in graph[node]:
            pq.append((node, neighbor, graph[node][neighbor]))

    # Sort the priority queue by edge weight
    pq.sort(key=lambda x: x[2])

    # Create a disjoint set to store the connected components
    dsu = DisjointSet(len(graph))

    # Iterate through the priority queue and add edges to the MST
    mst = []
    while pq:
        node1, node2, weight = pq.pop(0)
        if dsu.find(node1) != dsu.find(node2):
            mst.append((node1, node2))
            dsu.union(node1, node2)

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


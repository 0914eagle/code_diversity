
def get_cost(n, m, p, insecure_buildings, cost_matrix):
    # Initialize the graph with the given cost matrix
    graph = cost_matrix

    # Add the insecure buildings to the graph
    for building in insecure_buildings:
        graph[building][building] = 0

    # Find the minimum spanning tree of the graph
    mst = kruskal(graph)

    # Calculate the total cost of the MST
    total_cost = 0
    for edge in mst:
        total_cost += graph[edge[0]][edge[1]]

    return total_cost

def kruskal(graph):
    # Initialize the disjoint set with all the buildings
    disjoint_set = DisjointSet(graph.shape[0])

    # Sort the edges of the graph by their weight
    edges = sorted(graph, key=lambda x: x[2])

    # Iterate through the sorted edges
    for edge in edges:
        # Check if the two buildings are not in the same set
        if not disjoint_set.find(edge[0]) == disjoint_set.find(edge[1]):
            # Add the edge to the MST
            mst.append(edge)

            # Union the two sets
            disjoint_set.union(edge[0], edge[1])

    return mst

class DisjointSet:
    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n
        self.n = n

    def find(self, node):
        if self.parents[node] == -1:
            return node
        else:
            self.parents[node] = self.find(self.parents[node])
            return self.parents[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if self.ranks[root1] > self.ranks[root2]:
            self.parents[root2] = root1
        elif self.ranks[root1] < self.ranks[root2]:
            self.parents[root1] = root2
        else:
            self.parents[root2] = root1
            self.ranks[root1] += 1

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    cost_matrix = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        cost_matrix.append([x, y, cost])
    cost = get_cost(n, m, p, insecure_buildings, cost_matrix)
    print(cost)

if __name__ == '__main__':
    main()


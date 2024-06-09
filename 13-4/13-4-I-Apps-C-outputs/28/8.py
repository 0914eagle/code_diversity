
def get_cheapest_network(n, m, p, insecure_buildings, direct_connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the direct connections
    for x, y, cost in direct_connections:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum spanning tree of the graph
    mst = kruskal(graph)

    # Initialize the total cost of the network to 0
    total_cost = 0

    # Iterate through the edges of the MST
    for edge in mst:
        # If the edge connects two insecure buildings, do not include it in the network
        if edge[0] in insecure_buildings and edge[1] in insecure_buildings:
            continue
        # If the edge connects an insecure building to a secure building, include it in the network
        if edge[0] in insecure_buildings or edge[1] in insecure_buildings:
            total_cost += edge[2]

    return total_cost

def kruskal(graph):
    # Initialize the minimum spanning tree with 0 edges
    mst = []

    # Sort the edges of the graph by weight in non-decreasing order
    edges = [(weight, node1, node2) for node1, edges in enumerate(graph) for node2, weight in edges]
    edges.sort(key=lambda x: x[0])

    # Initialize the disjoint set with n subsets
    disjoint_set = [i for i in range(len(graph))]

    # Iterate through the sorted edges
    for edge in edges:
        # If the edge connects two buildings in different subsets, add it to the MST
        if find_set(disjoint_set, edge[1]) != find_set(disjoint_set, edge[2]):
            mst.append(edge)
            union_sets(disjoint_set, edge[1], edge[2])

    return mst

def find_set(disjoint_set, node):
    # Find the root of the subset that the node belongs to
    if disjoint_set[node] != node:
        disjoint_set[node] = find_set(disjoint_set, disjoint_set[node])
    return disjoint_set[node]

def union_sets(disjoint_set, node1, node2):
    # Union the subsets of the two nodes
    root1 = find_set(disjoint_set, node1)
    root2 = find_set(disjoint_set, node2)
    disjoint_set[root1] = root2

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    direct_connections = [tuple(map(int, input().split())) for _ in range(m)]
    print(get_cheapest_network(n, m, p, insecure_buildings, direct_connections))


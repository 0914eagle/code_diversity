
def get_bridges(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a variable to store the number of bridges
    bridges = 0

    # Iterate over the edges and check if they are bridges
    for edge in edges:
        # If the edge is a bridge, increment the number of bridges
        if is_bridge(graph, edge[0], edge[1]):
            bridges += 1

    return bridges

# Check if an edge is a bridge
def is_bridge(graph, u, v):
    # If either vertex is not connected to the other vertex, the edge is a bridge
    if u not in graph[v] or v not in graph[u]:
        return True
    return False


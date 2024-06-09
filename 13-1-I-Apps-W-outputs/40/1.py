
def min_separate_cities(n, m, roads):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
        graph[road[1] - 1].append(road[0] - 1)

    # Initialize a set to store the separate cities
    separate_cities = set()

    # Iterate through the graph
    for node in range(n):
        # If the node is not visited, do a DFS traversal from that node
        if node not in separate_cities:
            dfs_traversal(graph, node, separate_cities)

    # Return the number of separate cities
    return len(separate_cities)

def dfs_traversal(graph, node, separate_cities):
    # Mark the current node as visited
    separate_cities.add(node)

    # Recursively traverse the graph from the current node
    for neighbor in graph[node]:
        if neighbor not in separate_cities:
            dfs_traversal(graph, neighbor, separate_cities)



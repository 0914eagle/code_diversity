
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
        # If the node is not in the separate cities set, explore its neighbors
        if node not in separate_cities:
            # Explore the node's neighbors and mark them as separate cities
            explore_neighbors(graph, node, separate_cities)

    # Return the number of separate cities
    return len(separate_cities)

def explore_neighbors(graph, node, separate_cities):
    # Mark the current node as a separate city
    separate_cities.add(node)

    # Explore the node's neighbors
    for neighbor in graph[node]:
        # If the neighbor is not in the separate cities set, explore its neighbors
        if neighbor not in separate_cities:
            explore_neighbors(graph, neighbor, separate_cities)



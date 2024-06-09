
def solve(n, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Find all centroids in the graph
    centroids = []
    for vertex in range(n):
        if is_centroid(graph, vertex):
            centroids.append(vertex)

    # If there is only one centroid, return it
    if len(centroids) == 1:
        return centroids[0] + 1

    # If there are multiple centroids, find the pair of vertices that connects them
    for centroid in centroids:
        for other_centroid in centroids:
            if other_centroid != centroid and is_connected(graph, centroid, other_centroid):
                return centroid + 1, other_centroid + 1

    # If no pair of vertices connects the centroids, return an empty tuple
    return ()

def is_centroid(graph, vertex):
    # Remove the vertex and all edges from it
    graph_copy = graph[:]
    graph_copy[vertex] = []
    for i in range(len(graph_copy)):
        if vertex in graph_copy[i]:
            graph_copy[i].remove(vertex)

    # Find the largest connected component in the graph
    largest_component = []
    for i in range(len(graph_copy)):
        if i not in largest_component:
            largest_component.extend(dfs(graph_copy, i))

    # Return True if the largest connected component has the maximum size
    return len(largest_component) == len(graph)

def is_connected(graph, vertex1, vertex2):
    # Check if there is a path between vertex1 and vertex2 in the graph
    queue = [vertex1]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex == vertex2:
            return True
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
    return False

def dfs(graph, vertex):
    # Depth-first search to find all vertices connected to vertex
    visited = set()
    queue = [vertex]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
    return visited


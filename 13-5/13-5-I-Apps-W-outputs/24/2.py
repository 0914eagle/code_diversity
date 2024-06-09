
def solve(n, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Find the centroid of the graph
    centroid = find_centroid(graph)

    # Cut the edge between the centroid and any other vertex
    x, y = centroid, 1
    while y in graph[x - 1]:
        y += 1
    graph[x - 1].remove(y)
    graph[y - 1].remove(x)

    # Add the edge between the centroid and any other vertex
    x, y = centroid, 1
    while y in graph[x - 1]:
        y += 1
    graph[x - 1].append(y)
    graph[y - 1].append(x)

    return x, y

def find_centroid(graph):
    # Initialize the centroid as the first vertex
    centroid = 1

    # Iterate through the vertices of the graph
    for vertex in range(1, len(graph)):
        # If the vertex is not in the graph, skip it
        if vertex not in graph[centroid - 1]:
            continue

        # If the vertex is in the graph, check if it is a centroid
        if len(graph[vertex - 1]) < len(graph[centroid - 1]):
            centroid = vertex

    return centroid


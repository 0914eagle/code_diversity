
def get_maximum_edges(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize variables to store the maximum number of edges and the vertices with the maximum number of edges
    max_edges = 0
    max_vertices = []

    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # If the vertices are not connected, skip this pair
            if j not in graph[i]:
                continue
            # If the vertices are connected, find the number of edges between them
            num_edges = 0
            queue = [i]
            visited = set()
            while queue:
                vertex = queue.pop(0)
                if vertex not in visited:
                    visited.add(vertex)
                    queue += graph[vertex]
                    num_edges += 1
            # If the number of edges is greater than the maximum number of edges, update the maximum number of edges and the vertices with the maximum number of edges
            if num_edges > max_edges:
                max_edges = num_edges
                max_vertices = [i, j]

    return max_edges, max_vertices


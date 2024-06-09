
def get_bridges(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a queue to do BFS
    queue = []

    # Initialize a dictionary to keep track of the number of edges to each vertex
    edges_to_vertex = {}
    for i in range(1, n+1):
        edges_to_vertex[i] = 0

    # Initialize a dictionary to keep track of the bridges
    bridges = {}
    for i in range(1, m+1):
        bridges[i] = False

    # Do BFS starting from vertex 1
    queue.append(1)
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in edges_to_vertex:
                queue.append(neighbor)
                edges_to_vertex[neighbor] = edges_to_vertex[vertex] + 1
            elif edges_to_vertex[neighbor] == edges_to_vertex[vertex] + 1:
                # If we find a vertex that is connected to the current vertex through a bridge, mark it as a bridge
                bridges[edges_to_vertex[neighbor]] = True

    # Return the number of bridges
    return sum(bridges.values())


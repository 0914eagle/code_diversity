
def get_bridges(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a queue to do a BFS traversal of the graph
    queue = []

    # Initialize a dictionary to keep track of the number of edges to each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0

    # Do a BFS traversal of the graph
    queue.append(1)
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in degrees:
                queue.append(neighbor)
                degrees[neighbor] = 1
            else:
                degrees[neighbor] += 1

    # Find the bridges
    bridges = 0
    for edge in edges:
        if degrees[edge[0]] == 1 or degrees[edge[1]] == 1:
            bridges += 1

    return bridges


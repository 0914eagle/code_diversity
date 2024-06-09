
def get_network_topology(n, m, edges):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Check if the graph is connected
    if not is_connected(graph):
        return "unknown topology"

    # Check if the graph is a bus
    if is_bus(graph):
        return "bus topology"

    # Check if the graph is a ring
    if is_ring(graph):
        return "ring topology"

    # Check if the graph is a star
    if is_star(graph):
        return "star topology"

    # If none of the above conditions are met, the graph is unknown
    return "unknown topology"

# Check if the graph is connected
def is_connected(graph):
    visited = [False] * len(graph)
    queue = [0]
    visited[0] = True

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor - 1]:
                visited[neighbor - 1] = True
                queue.append(neighbor)

    for node in visited:
        if not node:
            return False

    return True

# Check if the graph is a bus
def is_bus(graph):
    visited = [False] * len(graph)
    queue = [0]
    visited[0] = True

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor - 1]:
                visited[neighbor - 1] = True
                queue.append(neighbor)

    return all(visited[1:])

# Check if the graph is a ring
def is_ring(graph):
    visited = [False] * len(graph)
    queue = [0]
    visited[0] = True

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor - 1]:
                visited[neighbor - 1] = True
                queue.append(neighbor)

    return all(visited[1:]) and visited[0]

# Check if the graph is a star
def is_star(graph):
    center = 0
    visited = [False] * len(graph)
    queue = [0]
    visited[0] = True

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor - 1]:
                visited[neighbor - 1] = True
                queue.append(neighbor)

    return all(visited[1:]) and visited[0]


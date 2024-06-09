
def get_network_topology(n, m, edges):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Check if the graph is connected
    visited = [False] * n
    queue = [0]
    visited[0] = True
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor - 1]:
                visited[neighbor - 1] = True
                queue.append(neighbor)

    # Check if the graph is a bus, ring, or star
    if len(set(visited)) == 1:
        return "bus topology"
    elif all(len(neighbors) == 2 for neighbors in graph):
        return "ring topology"
    elif len(set(visited)) == 2:
        return "star topology"
    else:
        return "unknown topology"


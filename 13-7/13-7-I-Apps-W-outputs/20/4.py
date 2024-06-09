
def find_network_topology(n, m, edges):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Check if the graph is connected
    visited = [False] * n
    queue = [0]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            queue += graph[node]

    if not all(visited):
        return "unknown topology"

    # Check if the graph is a bus, ring, or star
    if len(edges) == n - 1:
        return "bus topology"
    elif len(edges) == n - 2:
        return "ring topology"
    elif len(edges) == n - 3:
        return "star topology"
    else:
        return "unknown topology"


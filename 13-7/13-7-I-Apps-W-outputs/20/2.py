
def get_network_topology(n, m, edges):
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

    if all(visited):
        # Check if the graph is a bus
        if len(edges) == n - 1 and all(len(graph[i]) == 2 for i in range(n)):
            return "bus topology"
        # Check if the graph is a ring
        if len(edges) == n and all(len(graph[i]) == 2 for i in range(n)):
            return "ring topology"
        # Check if the graph is a star
        if len(edges) == n - 1 and all(len(graph[i]) == 1 for i in range(n)):
            return "star topology"

    return "unknown topology"


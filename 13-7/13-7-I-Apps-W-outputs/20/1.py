
def get_network_topology(n, m, edges):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[edges[i][0] - 1].append(edges[i][1] - 1)
        graph[edges[i][1] - 1].append(edges[i][0] - 1)

    # Check if the graph is connected
    visited = [False] * n
    queue = [0]
    visited[0] = True
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # Check if the graph is a bus, ring, or star
    if all(len(graph[i]) == 2 for i in range(n)):
        return "bus topology"
    elif all(len(graph[i]) == 1 for i in range(n)):
        return "star topology"
    elif all(len(graph[i]) == 2 for i in range(n - 1)):
        return "ring topology"
    else:
        return "unknown topology"



def is_possible(n, m, roads):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
        graph[road[1] - 1].append(road[0] - 1)

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

    # If the graph is connected, return YES and a possible direction assignment
    if visited.count(True) == n:
        return "YES"

    # If the graph is not connected, return NO
    return "NO"


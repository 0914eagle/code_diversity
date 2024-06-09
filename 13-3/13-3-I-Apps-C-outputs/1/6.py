
def solve(N, M, roads):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
        graph[road[1] - 1].append(road[0] - 1)

    # Check if the graph is connected
    visited = [False] * N
    queue = [0]
    visited[0] = True
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # If the graph is not connected, return "NO"
    if not all(visited):
        return "NO"

    # If the graph is connected, return "YES" and a possible direction assignment
    direction = []
    for road in roads:
        if road[0] != 1:
            direction.append([road[0], road[1]])
        else:
            direction.append([road[1], road[0]])
    return "YES\n" + "\n".join(str(road) for road in direction)


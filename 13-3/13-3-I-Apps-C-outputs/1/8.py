
def solve(N, M, roads):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for x, y in roads:
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
    
    # Check if the graph is connected
    visited = [False] * N
    queue = [0]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            queue.extend(graph[node])
    
    # If the graph is not connected, return "NO"
    if not all(visited):
        return "NO"
    
    # If the graph is connected, return "YES" and a direction assignment for each road
    directions = []
    for x, y in roads:
        if x < y:
            directions.append([x, y])
        else:
            directions.append([y, x])
    return "YES\n" + "\n".join(str(x) + " " + str(y) for x, y in directions)


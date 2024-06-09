
def get_unused_switches(n, m, cables):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the cables
    for a, b, length in cables:
        graph[a - 1].append((b - 1, length))
        graph[b - 1].append((a - 1, length))

    # Find the shortest path between switch 1 and switch n
    visited = [False] * n
    queue = [(0, 1)]
    while queue:
        dist, curr = queue.pop(0)
        if curr == n - 1:
            break
        for neighbor, length in graph[curr]:
            if not visited[neighbor]:
                queue.append((dist + length, neighbor))
                visited[neighbor] = True

    # Find the switches that are not in the shortest path
    unused_switches = []
    for i in range(n):
        if i + 1 not in visited:
            unused_switches.append(i + 1)

    return len(unused_switches), sorted(unused_switches)


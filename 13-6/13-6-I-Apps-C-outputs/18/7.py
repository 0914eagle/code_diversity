
def get_unused_switches(n, m, cables):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for a, b, length in cables:
        graph[a - 1].append((b - 1, length))
        graph[b - 1].append((a - 1, length))
    
    # Find the shortest path from switch 1 to switch n
    visited = [False] * n
    queue = [(0, 1)]
    while queue:
        distance, node = queue.pop(0)
        if node == n - 1:
            break
        for neighbor, length in graph[node]:
            if not visited[neighbor]:
                queue.append((distance + length, neighbor))
                visited[neighbor] = True
    
    # Find the switches that are not in the shortest path
    unused_switches = []
    for i in range(n):
        if i + 1 not in visited:
            unused_switches.append(i + 1)
    
    return len(unused_switches), unused_switches


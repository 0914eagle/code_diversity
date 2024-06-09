
def solve(n, m, edges, s, t):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find the shortest path between the initial stations of Alice and Bob
    visited = set()
    queue = [(s, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node == t:
            return distance
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append((neighbor, distance + 1))
    
    return "never meet"


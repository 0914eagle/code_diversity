
def solve(n, m, neighbors, s, t):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in neighbors:
        graph[u].append(v)
        graph[v].append(u)
    
    # Breadth-first search to find the shortest path between s and t
    queue = [(s, 0)]
    visited = set()
    while queue:
        node, distance = queue.pop(0)
        if node == t:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, distance + 1))
    
    return "never meet"


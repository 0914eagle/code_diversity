
def maximize_reachable_vertices(n, m, s, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for t, u, v in edges:
        if t == 1:
            graph[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)
    
    visited = [False] * (n + 1)
    visited[s] = True
    stack = [s]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    
    reachable_vertices = sum(visited) - 1  # Excluding the starting vertex
    orientations = ['+' if t == 2 and visited[u] and visited[v] else '-' for t, u, v in edges]
    
    return reachable_vertices, ''.join(orientations)

def minimize_reachable_vertices(n, m, s, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for t, u, v in edges:
        if t == 1:
            graph[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)
    
    visited = [False] * (n + 1)
    visited[s] = True
    stack = [s]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    
    reachable_vertices = sum(visited) - 1  # Excluding the starting vertex
    orientations = ['+' if t == 2 and not visited[u] and not visited[v] else '-' for t, u, v in edges]
    
    return reachable_vertices, ''.join(orientations)

if __name__ == "__main__":
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    max_reachable_vertices, max_orientations = maximize_reachable_vertices(n, m, s, edges)
    min_reachable_vertices, min_orientations = minimize_reachable_vertices(n, m, s, edges)

    print(max_reachable_vertices)
    print(max_orientations)
    print(min_reachable_vertices)
    print(min_orientations)

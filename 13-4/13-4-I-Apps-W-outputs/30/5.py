
def is_tourist_friendly(graph):
    n = len(graph)
    visited = [False] * n
    stack = [0]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
    return all(visited)

def solve(graph):
    n = len(graph)
    m = len(graph[0])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = 0
                if is_tourist_friendly(graph):
                    return "YES"
                graph[i][j] = 1
    return "NO"


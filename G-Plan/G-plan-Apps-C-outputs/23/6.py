_maximize_reachable_vertices(n, m, s, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for t, u, v in edges:
        if t == 1:
            graph[u].append(v)
            graph[v].append(u)
        else:
            graph[u].append(v)
            graph[v].append(u)
    
    visited = [False] * (n + 1)
    reachable_vertices = 0
    orientations = []
    
    def dfs(node):
        nonlocal reachable_vertices
        visited[node] = True
        reachable_vertices += 1
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                orientations.append((node, neighbor))
                dfs(neighbor)
    
    dfs(s)
    
    print(reachable_vertices)
    for u, v in edges:
        if (u, v) in orientations:
            print('+', end='')
        else:
            print('-', end='')
    print()

def plan_minimize_reachable_vertices(n, m, s, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for t, u, v in edges:
        if t == 1:
            graph[u].append(v)
            graph[v].append(u)
        else:
            graph[u].append(v)
            graph[v].append(u)
    
    visited = [False] * (n + 1)
    reachable_vertices = 0
    orientations = []
    
    def dfs(node):
        nonlocal reachable_vertices
        visited[node] = True
        reachable_vertices += 1
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                orientations.append((node, neighbor))
                dfs(neighbor)
    
    dfs(s)
    
    print(reachable_vertices)
    for u, v in edges:
        if (u, v) in orientations:
            print('+', end='')
        else:
            print('-', end='')
    print()

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    
    plan_maximize_reachable_vertices(n, m, s, edges)
    plan_minimize_reachable_vertices(n, m, s, edges)

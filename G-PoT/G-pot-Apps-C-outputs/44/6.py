
from collections import defaultdict

def find_safe_routes(n, h, routes):
    adj_list = defaultdict(list)
    for a, b in routes:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    visited = [False] * n
    parent = [-1] * n
    safe_routes = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                dfs(neighbor)
    
    dfs(h)
    
    for i in range(n):
        if not visited[i]:
            safe_routes.append((parent[i], i))
    
    return len(safe_routes), safe_routes

# Input
n, h = map(int, input().split())
routes = [tuple(map(int, input().split())) for _ in range(n-1)]

# Output
m, new_routes = find_safe_routes(n, h, routes)
print(m)
for a, b in new_routes:
    print(a, b)

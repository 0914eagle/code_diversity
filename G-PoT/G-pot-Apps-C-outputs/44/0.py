
def find_additional_routes(n, h, routes):
    graph = {}
    for a, b in routes:
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    
    visited = set()
    safe_routes = set()
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                if neighbor != h:
                    safe_routes.add((node, neighbor))
    
    dfs(h)
    
    additional_routes = []
    for a, b in routes:
        if (a, b) not in safe_routes and (b, a) not in safe_routes:
            additional_routes.append((a, b))
    
    return len(additional_routes), additional_routes

# Input
n, h = map(int, input().split())
routes = [tuple(map(int, input().split())) for _ in range(n-1)]

# Output
m, additional_routes = find_additional_routes(n, h, routes)
print(m)
for a, b in additional_routes:
    print(a, b)

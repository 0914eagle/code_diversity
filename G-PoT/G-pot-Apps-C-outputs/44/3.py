
def find_escape_routes(n, h, routes):
    adj_list = [[] for _ in range(n)]
    for a, b in routes:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    visited = [False] * n
    visited[h] = True
    queue = [h]
    while queue:
        current = queue.pop(0)
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    missing_routes = []
    for i in range(n):
        if not visited[i]:
            missing_routes.append((h, i))
    
    return len(missing_routes), missing_routes

# Input
n, h = map(int, input().split())
routes = [tuple(map(int, input().split())) for _ in range(n-1)]

# Output
m, missing_routes = find_escape_routes(n, h, routes)
print(m)
for a, b in missing_routes:
    print(a, b)

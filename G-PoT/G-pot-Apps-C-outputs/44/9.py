
from collections import defaultdict

def add_escape_routes(n, h, routes):
    adj_list = defaultdict(list)
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
    
    to_add = []
    for i in range(n):
        if not visited[i]:
            to_add.append((h, i))
    
    return len(to_add), to_add

# Input
n, h = map(int, input().split())
routes = [tuple(map(int, input().split())) for _ in range(n-1)]

# Output
m, added_routes = add_escape_routes(n, h, routes)
print(m)
for a, b in added_routes:
    print(a, b)

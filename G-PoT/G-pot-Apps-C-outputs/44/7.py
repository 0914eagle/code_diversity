
def find_min_passageways(n, h, routes):
    adj_list = [[] for _ in range(n)]
    for a, b in routes:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    visited = [False] * n
    visited[h] = True
    
    def dfs(node):
        nonlocal visited
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(h)
    
    to_add = []
    for i in range(n):
        if not visited[i]:
            to_add.append((h, i))
    
    return len(to_add), to_add

# Input
n, h = map(int, input().split())
routes = [tuple(map(int, input().split())) for _ in range(n-1)]

# Output
m, additional_passageways = find_min_passageways(n, h, routes)
print(m)
for a, b in additional_passageways:
    print(a, b)

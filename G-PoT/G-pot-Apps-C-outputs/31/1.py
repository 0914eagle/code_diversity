
from collections import defaultdict

def dfs(v, parent, edges, a, controls):
    count = 0
    for u, w in edges[v]:
        if u != parent:
            count += dfs(u, v, edges, a, controls)
    controls[v] = count
    for u, w in edges[v]:
        if u != parent and a[u] >= w:
            controls[v] += controls[u] + 1
    return count

n = int(input())
a = list(map(int, input().split()))
edges = defaultdict(list)
for _ in range(n - 1):
    p, w = map(int, input().split())
    edges[p - 1].append((_, w))

controls = [0] * n
dfs(0, -1, edges, a, controls)

print(*controls)

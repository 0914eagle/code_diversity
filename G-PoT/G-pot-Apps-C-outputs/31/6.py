
from collections import defaultdict

def dfs(v, parent, dist, a, edges, controls):
    cnt = 0
    for u, w in edges[v]:
        if u != parent:
            cnt += dfs(u, v, dist + w, a, edges, controls)
    controls[v] = cnt
    for u, w in edges[v]:
        if u != parent and dist + w <= a[u]:
            cnt += 1 + controls[u]
    return cnt

n = int(input())
a = list(map(int, input().split()))
edges = defaultdict(list)
for _ in range(n-1):
    p, w = map(int, input().split())
    edges[p-1].append((_, w))

controls = [0] * n
dfs(0, -1, 0, a, edges, controls)

print(*controls)

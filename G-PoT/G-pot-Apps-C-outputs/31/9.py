
from collections import defaultdict

def dfs(v, parent, dist, a, edges, controls):
    count = 0
    for u, w in edges[v]:
        if u != parent:
            new_dist = min(dist + w, a[u])
            count += dfs(u, v, new_dist, a, edges, controls)
    controls[v] = count
    return count + 1

n = int(input())
a = list(map(int, input().split()))
edges = defaultdict(list)
for _ in range(n - 1):
    p, w = map(int, input().split())
    edges[p - 1].append((_, w))

controls = [0] * n
dfs(0, -1, 0, a, edges, controls)
print(*controls)

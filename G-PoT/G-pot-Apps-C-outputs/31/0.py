
from collections import defaultdict

def dfs(v, parent, dist, a, edge_weights, controls):
    count = 0
    for u, w in controls[v]:
        if u != parent:
            new_dist = min(dist + w, a[u])
            count += dfs(u, v, new_dist, a, edge_weights, controls)
    return count + 1

n = int(input())
a = list(map(int, input().split()))

controls = defaultdict(list)
for _ in range(n-1):
    p, w = map(int, input().split())
    controls[p-1].append((_, w))

result = []
for i in range(n):
    result.append(dfs(i, -1, 0, a, controls, controls))

print(*result)

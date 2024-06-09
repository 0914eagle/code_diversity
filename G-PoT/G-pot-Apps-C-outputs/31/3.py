
from collections import defaultdict

def dfs(v, parent, dist, a, edges, controls):
    num_controls = 0
    for u, w in edges[v]:
        if u != parent:
            new_dist = dist + w
            if new_dist <= a[u-1]:
                num_controls += 1
            num_controls += dfs(u, v, new_dist, a, edges, controls)
    controls[v] = num_controls
    return num_controls

n = int(input())
a = list(map(int, input().split()))
edges = defaultdict(list)
for _ in range(n-1):
    p, w = map(int, input().split())
    edges[p].append((_, w))
controls = [0] * n
dfs(1, 0, 0, a, edges, controls)
print(*controls)

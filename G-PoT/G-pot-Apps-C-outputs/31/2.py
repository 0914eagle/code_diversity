
from collections import defaultdict

def dfs(v, parent, dist, a, graph, control_count):
    count = 0
    for u, w in graph[v]:
        if u == parent:
            continue
        if dist + w <= a[u-1]:
            count += 1
            control_count[v-1] += 1
        count += dfs(u, v, max(0, dist + w), a, graph, control_count)
    return count

n = int(input())
a = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n-1):
    p, w = map(int, input().split())
    graph[p].append((p+1, w))

control_count = [0] * n
dfs(1, -1, 0, a, graph, control_count)

print(*control_count)

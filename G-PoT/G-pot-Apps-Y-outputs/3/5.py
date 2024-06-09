
from collections import defaultdict

def dfs(node, parent, dist, total_dist, values):
    total_dist[node] = values[node]
    for child in graph[node]:
        if child != parent:
            total_dist[node] += dfs(child, node, dist, total_dist, values)
            dist[node] += dist[child] + total_dist[child]
    return total_dist[node]

n = int(input())
values = list(map(int, input().split()))
graph = defaultdict(list)
dist = [0] * n
total_dist = [0] * n

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

dfs(0, -1, dist, total_dist, values)

max_cost = sum(dist[i] * values[i] for i in range(n))
print(max_cost)


from collections import defaultdict

def dfs(node, parent, dist, value, total_dist, total_value):
    total_value[node] = value[node]
    total_dist[node] = dist[node]
    
    for child in graph[node]:
        if child != parent:
            dfs(child, node, dist+1, value, total_dist, total_value)
            total_value[node] += total_value[child]
            total_dist[node] += total_dist[child]

n = int(input())
values = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

total_dist = [0] * (n+1)
total_value = [0] * (n+1)

dfs(1, 0, 0, values, total_dist, total_value)

result = sum([total_dist[i] * values[i] for i in range(1, n+1)])
print(result)

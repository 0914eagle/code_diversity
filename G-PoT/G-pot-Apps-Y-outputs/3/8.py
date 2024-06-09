
from collections import defaultdict

def dfs(node, parent, dist, values, subtree_sum, total_sum):
    subtree_sum[node] = values[node-1]
    for child in graph[node]:
        if child != parent:
            dfs(child, node, dist+1, values, subtree_sum, total_sum)
            subtree_sum[node] += subtree_sum[child]
    total_sum[0] += dist * values[node-1] * subtree_sum[node]

n = int(input())
values = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

subtree_sum = [0] * (n+1)
total_sum = [0]
dfs(1, 0, 0, values, subtree_sum, total_sum)
print(total_sum[0])

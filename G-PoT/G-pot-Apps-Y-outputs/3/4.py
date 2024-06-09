
from collections import defaultdict

def dfs(node, parent, depth):
    global max_cost
    max_cost += depth * values[node]
    
    for child in graph[node]:
        if child != parent:
            dfs(child, node, depth + 1)

n = int(input())
values = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

max_cost = 0
dfs(1, 0, 0)

print(max_cost)

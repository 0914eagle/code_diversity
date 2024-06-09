
def dfs(node, parent, depth):
    global max_cost
    cost = depth * values[node]
    max_cost = max(max_cost, cost)
    
    for child in graph[node]:
        if child != parent:
            dfs(child, node, depth + 1)

n = int(input())
values = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

max_cost = 0
dfs(0, -1, 0)
print(max_cost)

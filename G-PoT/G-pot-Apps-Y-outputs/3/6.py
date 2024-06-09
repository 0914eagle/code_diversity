
from collections import defaultdict

def dfs(node, parent, depth, values, tree, total_cost):
    total_cost[node] = depth * values[node]
    for child in tree[node]:
        if child != parent:
            total_cost[node] += dfs(child, node, depth + 1, values, tree, total_cost)
    return total_cost[node]

n = int(input())
values = list(map(int, input().split()))
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

total_cost = [0] * (n+1)
dfs(1, 0, 0, values, tree, total_cost)

max_cost = max(total_cost)
print(max_cost)

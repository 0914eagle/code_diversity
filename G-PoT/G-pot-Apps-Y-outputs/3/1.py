
from collections import defaultdict

def dfs(node, parent, depth, values, tree, total_cost):
    cost = depth * values[node]
    total_cost += cost
    for child in tree[node]:
        if child != parent:
            total_cost = dfs(child, node, depth + 1, values, tree, total_cost)
    return total_cost

n = int(input())
values = list(map(int, input().split()))
tree = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

total_cost = dfs(1, -1, 0, values, tree, 0)
print(total_cost)

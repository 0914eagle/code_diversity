
from collections import defaultdict

def dfs(node, parent, depth, values, tree, subtree_sum):
    subtree_sum[node] = values[node-1]
    for child in tree[node]:
        if child != parent:
            subtree_sum[node] += dfs(child, node, depth+1, values, tree, subtree_sum)
    return subtree_sum[node]

def calculate_cost(node, parent, depth, values, tree, subtree_sum, total_sum):
    total_sum += depth * values[node-1]
    for child in tree[node]:
        if child != parent:
            total_sum = calculate_cost(child, node, depth+1, values, tree, subtree_sum, total_sum)
    return total_sum

n = int(input())
values = list(map(int, input().split()))
tree = defaultdict(list)
subtree_sum = [0] * (n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1, 0, 0, values, tree, subtree_sum)
total_sum = calculate_cost(1, 0, 0, values, tree, subtree_sum, 0)
print(total_sum)

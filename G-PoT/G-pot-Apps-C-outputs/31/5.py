
from collections import defaultdict

def dfs(node, parent, dist, a, controls):
    count = 0
    for child, edge_weight in tree[node]:
        if child != parent:
            new_dist = min(dist + edge_weight, a[child-1])
            count += dfs(child, node, new_dist, a, controls)
    controls[node] = count
    return count + 1

n = int(input())
a = list(map(int, input().split()))
tree = defaultdict(list)
for _ in range(n-1):
    p, w = map(int, input().split())
    tree[p].append((_, w))

controls = [0] * n
dfs(1, -1, 0, a, controls)

print(" ".join(map(str, controls)))

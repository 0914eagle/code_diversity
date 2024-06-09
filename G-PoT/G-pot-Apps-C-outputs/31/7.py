
from collections import defaultdict

def dfs(node, parent, edges, a_values, controls):
    count = 0
    for child, weight in edges[node]:
        if child != parent:
            count += dfs(child, node, edges, a_values, controls)
            controls[node] += controls[child]
            if a_values[child] >= weight:
                controls[node] += 1
    return count + 1

n = int(input())
a_values = list(map(int, input().split()))
edges = defaultdict(list)
for _ in range(n - 1):
    parent, weight = map(int, input().split())
    edges[parent].append((_, weight))

controls = [0] * n
dfs(1, -1, edges, a_values, controls)

print(' '.join(map(str, controls)))

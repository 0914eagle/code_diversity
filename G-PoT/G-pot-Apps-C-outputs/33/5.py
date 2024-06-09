
def dfs(node, values, children):
    max_subset = 1
    for child in children[node]:
        max_subset = max(max_subset, 1 + dfs(child, values, children))
    return max_subset

n = int(input())
values = [0] * (n+1)
parents = [0] * (n+1)
children = [[] for _ in range(n+1)]

for i in range(1, n+1):
    v, p = map(int, input().split())
    values[i] = v
    parents[i] = p
    children[p].append(i)

result = dfs(1, values, children)
print(result)

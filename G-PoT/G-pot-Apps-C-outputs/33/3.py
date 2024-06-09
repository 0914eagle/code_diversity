
def dfs(node, values, children):
    if not children[node]:
        return 1
    max_subset = 1
    for child in children[node]:
        max_subset = max(max_subset, dfs(child, values, children))
    if all(values[node] > values[child] for child in children[node]):
        return max_subset + 1
    return max_subset

n = int(input())
values = [0] * (n+1)
children = [[] for _ in range(n+1)]

for i in range(1, n+1):
    v, p = map(int, input().split())
    values[i] = v
    children[p].append(i)

print(dfs(1, values, children))

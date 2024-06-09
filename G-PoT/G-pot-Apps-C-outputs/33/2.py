
def dfs(node, parent, values, children):
    max_heap_nodes = 1
    for child in children[node]:
        if values[node] > values[child]:
            max_heap_nodes += dfs(child, node, values, children)
    return max_heap_nodes

n = int(input())
values = [0] * (n+1)
parents = [0] * (n+1)
children = [[] for _ in range(n+1)]

for i in range(1, n+1):
    values[i], parents[i] = map(int, input().split())
    children[parents[i]].append(i)

result = dfs(1, 0, values, children)
print(result)

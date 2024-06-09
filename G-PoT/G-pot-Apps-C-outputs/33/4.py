
def dfs(node, values, children):
    if not children[node]:
        return 1, values[node]
    
    max_nodes = 1
    max_value = values[node]
    for child in children[node]:
        child_nodes, child_value = dfs(child, values, children)
        max_nodes += child_nodes
        max_value = max(max_value, child_value)
    
    if values[node] > max_value:
        return max_nodes, max_value
    else:
        return max_nodes, values[node]

n = int(input())
values = [0] * (n+1)
children = [[] for _ in range(n+1)]

for i in range(1, n+1):
    v, p = map(int, input().split())
    values[i] = v
    children[p].append(i)

max_nodes, _ = dfs(1, values, children)
print(max_nodes)

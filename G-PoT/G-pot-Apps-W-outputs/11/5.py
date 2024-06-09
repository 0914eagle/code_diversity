
def divide_items(N, items, M, pairs):
    graph = {}
    for item in items:
        graph[item] = set()
    
    for pair in pairs:
        item1, item2 = pair.split()
        graph[item1].add(item2)
        graph[item2].add(item1)
    
    visited = {}
    for item in items:
        visited[item] = False
    
    def dfs(node, group):
        visited[node] = True
        groups[group].add(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, 1 - group)
    
    groups = [set(), set()]
    for item in items:
        if not visited[item]:
            dfs(item, 0)
    
    if len(groups[0]) + len(groups[1]) == N:
        return groups[0], groups[1]
    else:
        return "impossible", "impossible"

# Read input
N = int(input())
items = [input() for _ in range(N)]
M = int(input())
pairs = [input() for _ in range(M)]

# Call the function and print output
walter_items, jesse_items = divide_items(N, items, M, pairs)
if walter_items == "impossible":
    print("impossible")
else:
    print(" ".join(walter_items))
    print(" ".join(jesse_items))

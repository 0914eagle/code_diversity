
N = int(input())
items = [input() for _ in range(N)]
M = int(input())
suspicious_pairs = [input().split() for _ in range(M)]

# Create a graph to represent the suspicious pairs
graph = {}
for pair in suspicious_pairs:
    item1, item2 = pair
    if item1 not in graph:
        graph[item1] = []
    if item2 not in graph:
        graph[item2] = []
    graph[item1].append(item2)
    graph[item2].append(item1)

# Perform a depth-first search to check if a valid division is possible
def dfs(item, group):
    visited.add(item)
    groups[group].append(item)
    for neighbor in graph.get(item, []):
        if neighbor not in visited:
            if not dfs(neighbor, 1 - group):
                return False
        elif neighbor in groups[group]:
            return False
    return True

visited = set()
groups = [[], []]
for item in items:
    if item not in visited:
        if not dfs(item, 0):
            print("impossible")
            break
else:
    print("\n".join(" ".join(group) for group in groups))

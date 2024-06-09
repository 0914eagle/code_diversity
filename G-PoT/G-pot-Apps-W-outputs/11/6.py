
def find_division(N, items, M, suspicious_pairs):
    graph = {}
    for item in items:
        graph[item] = set()

    for pair in suspicious_pairs:
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

    groups = [{}, {}]
    for item in items:
        if not visited[item]:
            dfs(item, 0)

    if len(groups[0]) + len(groups[1]) == N:
        return groups[0], groups[1]
    else:
        return "impossible"

N = int(input())
items = [input() for _ in range(N)]
M = int(input())
suspicious_pairs = [input() for _ in range(M)]

result = find_division(N, items, M, suspicious_pairs)
if result == "impossible":
    print("impossible")
else:
    for group in result:
        print(" ".join(group))

